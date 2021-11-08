from bs4 import BeautifulSoup, Tag
from selenium import webdriver
from time import sleep
import requests
from datetime import datetime
from pytz import timezone
from data import Index, code_to_name

def get_data():
    '''
    try:
        page = urlopen('https://www.tgju.org/currency')
    except URLError as e:
        print(e)
        exit()
    except HTTPError as e:
        print(e)
        exit()
    '''
      
    indexes = dict()
    AWAIT_TIME = 1
    
    #establish a chrome browser for real time scrap
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    browser = webdriver.Chrome(options=chrome_options)
    
    
    #get currency data
    browser.get('https://www.tgju.org/currency')
    sleep(AWAIT_TIME)
    
    page = browser.page_source
    page_bs = BeautifulSoup(page,'html.parser')

    price_table = page_bs.find_all('table',{'data-tab-id':"1"})

    print('-'*50)
    for table in price_table:
        for table_row in table.tbody.children:
            if isinstance(table_row, Tag):
                ind_code = table_row.get_attribute_list('data-market-row')[0].partition('_')[2]
                ind = Index(code_to_name(ind_code),
                                table_row.td.get_text(),
                                table_row.find_all('td')[4].get_text()
                                )
                indexes[ind_code] = ind

    #get coin data
    browser.get('https://www.tgju.org/coin')
    sleep(AWAIT_TIME)
    page = browser.page_source
    
    page_bs = BeautifulSoup(page,'html.parser')
    price_table = page_bs.find('table',{'class':"data-table market-table market-section-right"})

    for table_row in price_table.tbody.children:

        if isinstance(table_row, Tag):
            ind_code = table_row.get_attribute_list('data-market-row')[0]
            name = code_to_name(ind_code)
            price = table_row.td.get_text()
            time = table_row.find_all('td')[4].get_text()

            ind = Index(name, price, time)
            indexes[ind_code] = ind

    #get coin data
    browser.get('https://www.tgju.org/gold-chart')
    sleep(AWAIT_TIME)
    page = browser.page_source
       
    page_bs = BeautifulSoup(page,'html.parser')
    price_table = page_bs.find('table',{'data-tab-id':'1'})

    
    for table_row in price_table.tbody.children:

        if isinstance(table_row, Tag):
            ind_code = table_row.get_attribute_list('data-market-row')[0]
            name = code_to_name(ind_code)
            price = table_row.td.get_text()
            time = table_row.find_all('td')[4].get_text()

            ind = Index(name, price, time)
            indexes[ind_code] = ind
    
    
    browser.quit()
    
    #get gold world price
    headers = {
            'x-access-token': 'goldapi-4kzgtkvp8s6kt-io',
            'Content-Type': 'application/json'
            }
    data = requests.get('https://www.goldapi.io/api/XAU/USD', headers=headers)     
    data= data.json()
    price = data['price']
    t = datetime.fromtimestamp(data['timestamp'])
    time = t.astimezone(timezone('Asia/Tehran')).time()
     
    ind = Index('اونس جهانی طلا', price, time)
    indexes['goldoz'] = ind
    
    

    
    return indexes




data = get_data()

for key, value in data.items():
    print(f'cur {value.name} code is {key} and price is{value.value} and time{value.time}')

