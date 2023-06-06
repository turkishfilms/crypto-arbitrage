import requests
import json

def get_coingecko_prices(coin_symbols):
    with open("list.json","r") as conv:
        convert_to_id = json.load(conv)

    ids = ','.join([convert_to_id[coin.lower()] for coin in coin_symbols])

    url = 'https://api.coingecko.com/api/v3/'
    data = requests.get(url + 'coins/markets', params={
        'vs_currency': 'usd',
        'ids': ids,
        'order': 'market_cap_desc',
        'sparkline': False
    }).json()
   
    return {coin['symbol'].upper() : coin['current_price'] for coin in data}
            
if(__name__=="__main__"):
    pass

