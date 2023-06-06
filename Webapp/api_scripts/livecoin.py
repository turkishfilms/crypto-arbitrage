import requests
import json
import sys

sys.path.append("../")  

from temp.API_KEYS import livecoin_key

def get_livecoin_prices(coin_symbols):
    url = "https://api.livecoinwatch.com/coins/map"
    payload = json.dumps({
        "codes": coin_symbols,
        "currency": "USD",
        "meta": False
    })

    headers = {
    'content-type': 'application/json',
    'x-api-key': livecoin_key
    }  
    
    data = json.loads(requests.request("POST", url, headers=headers,data=payload).text)
    return { coin["code"]: coin["rate"] for coin in data}


if(__name__=="__main__"):
    pass