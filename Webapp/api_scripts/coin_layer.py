import sys
import requests
from datetime import date, timedelta

sys.path.append("../")  

from temp.API_KEYS import coinlayer_api_key2

def get_coinlayer_prices(coin_symbols):    
    url = "http://api.coinlayer.com/live?access_key=" + coinlayer_api_key2 + "&symbols=" + ','.join(coin_symbols)

    data = requests.get(url).json()
    return data["rates"]
    

def get_coinlayer_prices_yesterday(coin_symbols):
    yesterday = date.today()-timedelta(days=1)
    yesterdizzle = yesterday.isoformat()
    
    url = f"http://api.coinlayer.com/{yesterdizzle}?access_key=" + coinlayer_api_key2 + "&symbols=" + ','.join(coin_symbols) + "&expand=1"

    yesterdata  = requests.get(url).json()
    yestercoins = yesterdata["rates"]

    formatted_data={}
    for coin in yestercoins:
        formatted_data[coin] = {
        "Open":[yestercoins[coin]["rate"]],
        "High":[yestercoins[coin]["high"]],
        "Low":[yestercoins[coin]["low"]],
        "Close":[yestercoins[coin]["rate"]],
        "Adj Close":[yestercoins[coin]["rate"]],
        "Volume":[yestercoins[coin]["vol"]],
        "year":[yesterday.year],
        "month":[yesterday.month],
        "day":[yesterday.day],}
    return formatted_data 
    

if(__name__=="__main__"):
    pass