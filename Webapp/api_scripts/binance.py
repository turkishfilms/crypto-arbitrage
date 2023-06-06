import requests

def get_binance_prices(coin_symbols):
    symbols_str = ','.join([f'"{symbol}USD"' for symbol in coin_symbols])
    req = 'https://api.binance.us/api/v3/ticker/price?symbols=[' + symbols_str + ']'
    data = requests.get(req).json()
    return  {coin['symbol'][:-3]: float(coin['price']) for coin in data}

if(__name__=="__main__"):
    pass