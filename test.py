from urllib.request import urlopen
from bs4 import BeautifulSoup, Tag
from data import Index, code_to_name



page = urlopen('https://www.tgju.org/gold-chart')
page_bs = BeautifulSoup(page,'html.parser')
price_table = page_bs.find('table',{'data-tab-id':'1'})


for table_row in price_table.tbody.children:
    
    if isinstance(table_row, Tag):
        ind_code = table_row.get_attribute_list('data-market-row')[0]
        name = code_to_name(ind_code)
        price = table_row.td.get_text()
        time = table_row.find_all('td')[4].get_text()
       
        ind = Index(name, price, time)
        