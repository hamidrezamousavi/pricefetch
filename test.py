
import requests
from bs4 import BeautifulSoup


data = requests.get('http://www.tsetmc.com/Loader.aspx?ParTree=15')     
data_bs= BeautifulSoup(data.content.decode(),'html.parser')
price_tag = data_bs.table.find('td',text = 'شاخص کل').findNext('td')
price = price_tag.text.split(' ')[0]
print(price)