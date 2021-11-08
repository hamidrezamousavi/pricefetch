
import requests
from datetime import datetime

from pytz import timezone
headers = {
            'x-access-token': 'goldapi-4kzgtkvp8s6kt-io',
            'Content-Type': 'application/json'
            }
data = requests.get('https://www.goldapi.io/api/XAU/USD', headers=headers)     
data= data.json()

t = datetime.fromtimestamp(data['timestamp'])
t = t.astimezone(timezone('Asia/Tehran')) 
print(t.time(),data['price'])