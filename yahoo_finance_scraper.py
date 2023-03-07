import requests
from bs4 import BeautifulSoup
import json

myStocks = ['GAPW-B.ST', 'HANZA.ST', 'HYN.OL']
stockdata = []

def getData(symbol):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15'}
    url = f'https://finance.yahoo.com/quote/{symbol}'

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')

    stock = {
    'symbol': symbol,
    'price': soup.find('fin-streamer', {'class':'Fw(b) Fz(36px) Mb(-4px) D(ib)'}).text,
    'change': soup.find('fin-streamer', {'class': 'Fw(500) Pstart(8px) Fz(24px)'}).text,
    }
    return stock

for item in myStocks:
    stockdata.append(getData(item))
    print('Getting: ', item)

with open('stockdata.json', 'w') as f:
    json.dump(stockdata, f)

print('Finished!')