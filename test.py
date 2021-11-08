
import requests
import json

from requests.api import request




data = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd')

price = str(data.json()['bitcoin']['usd'])
name = 'بیت کوین'
ind_code = 'btc'
time = 'None'

ind = Index(name, price, time)
indexes[ind_code] = ind

print(price)