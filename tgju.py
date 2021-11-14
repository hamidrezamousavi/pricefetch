from bs4 import BeautifulSoup, Tag
from selenium import webdriver
from time import sleep
import requests
from datetime import datetime
from pytz import timezone
from data import Index, code_to_name



def get_data():
    '''
    this is coroutine that yield gathered data and related message 
    in 6 stages.Usage pattern of this coroutine is like below
    
    get_data = get_data()
    collected_data = dict()

    for data, msg in get_data:
        print(msg)
        collected_data = data
    '''
      
    indexes = dict()
    #this is time that script awatie to browse page update 
    AWAIT_TIME = 1
    
    #establish a chrome browser for real time scrap
     yield indexes, 'Gathering process is start'
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    browser = webdriver.Chrome(options=chrome_options)
    
    
    #get currency data
    try:
        browser.get('https://www.tgju.org/currency')
        sleep(AWAIT_TIME)

        page = browser.page_source
        page_bs = BeautifulSoup(page,'html.parser')

        price_table = page_bs.find_all('table',{'data-tab-id':"1"})


        for table in price_table:
            for table_row in table.tbody.children:
                if isinstance(table_row, Tag):
                    ind_code = table_row.get_attribute_list('data-market-row')[0].partition('_')[2]
                    ind = Index(code_to_name(ind_code),
                                    table_row.td.get_text(),
                                    table_row.find_all('td')[4].get_text()
                                    )
                    indexes[ind_code] = ind
        yield indexes,'Currency\'s data gathering is finished'
    except Exception as e:
        yield indexes, 'In currency : '+e
    
    #get coin data
    try:
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

        yield indexes,'Coin\'s data gathering is finished'
    except Exception as e:
        yield indexes, 'In coin : '+str(e)
    
    
    #get gold data
    try:
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

        yield indexes,'Gold\'s data gathering is finished'
    except Exception as e:
        yield indexes, 'In gold : '+str(e)
    

    browser.quit()
    
    #get gold world price
    try:
        headers = {
                'x-access-token': 'goldapi-4kzgtkvp8s6kt-io',
                'Content-Type': 'application/json'
                }
        data = requests.get('https://www.goldapi.io/api/XAU/USD', headers=headers)     
        data= data.json()
        price = data['price']
        t = datetime.fromtimestamp(data['timestamp'])
        time = t.astimezone(timezone('Asia/Tehran')).time()
        ind_code = 'goldoz'
        name = 'اونس جهانی طلا'
        ind = Index(name, price, time)
        indexes[ind_code] = ind

        yield indexes,'World Gold\'s data gathering is finished'
    except Exception as e:
        yield indexes, 'In world gold : '+str(e)
    
    #get bource index price
    try:
        data = requests.get('http://www.tsetmc.com/Loader.aspx?ParTree=15')     
        data_bs= BeautifulSoup(data.content.decode(),'html.parser')
        price_tag = data_bs.table.find('td',text = 'شاخص کل').findNext('td')

        price = price_tag.text.split(' ')[0]
        name = 'شاخص کل بورس'
        ind_code = 'bourcind'
        time = 'None'
        ind = Index(name, price, time)
        indexes[ind_code] = ind

        yield indexes,'Bource index\'s data gathering is finished'
    except Exception as e:
        yield indexes, 'In bource : '+str(e)
        
    #get bitcoin price
    try:
        data = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd')

        price = str(data.json()['bitcoin']['usd'])
        name = 'بیت کوین'
        ind_code = 'btc'
        time = 'None'

        ind = Index(name, price, time)
        indexes[ind_code] = ind
        yield indexes,'BitCoin\'s data gathering is finished'
    except Exception as e:
        yield indexes, 'In bitcoin : '+str(e)
    
    




#get_data = get_data()
#
#gather_data = dict()
#
#for data, msg in get_data:
#    print(msg)
#    gather_data = data
#    
#for key, value in gather_data.items():
#    print(f'cur {value.name} code is {key} and price is{value.value} and time{value.time}')
# 
#