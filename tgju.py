from bs4 import BeautifulSoup, Tag
from selenium import webdriver
from time import sleep
import requests
from datetime import datetime
from pytz import timezone
from data import Index, code_to_name, DateTime
import path


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
    #get system date
    date_time_now = DateTime()
    time_now= f'{date_time_now.hour}:{date_time_now.minute}:{date_time_now.second}'
    date_now = date_time_now.date
    #get currency data
    try:
       
        browser.get(path.currency_url)
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
                                    table_row.find_all('td')[4].get_text(),
                                    date_now
                                    )
                    indexes[ind_code] = ind
        yield indexes,'Currency\'s data gathering is finished'
    except Exception as e:
        yield indexes, 'In currency : '+ str(e)
    
    #get coin data
    try:
        browser.get(path.coin_url)
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

                ind = Index(name, price, time, date_now)
                indexes[ind_code] = ind

        yield indexes,'Coin\'s data gathering is finished'
    except Exception as e:
        yield indexes, 'In coin : '+str(e)
    
    
    #get gold data
    try:
        browser.get(path.gold_url)
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

                ind = Index(name, price, time, date_now)
                indexes[ind_code] = ind

        yield indexes,'Gold\'s data gathering is finished'
    except Exception as e:
        yield indexes, 'In gold : '+str(e)
    
    #get bource index price
    try:
        browser.get(path.bource_url)
        sleep(AWAIT_TIME)

        page = browser.page_source
        page_bs = BeautifulSoup(page,'html.parser')
        value = page_bs.find('li',{'id':'l-bourse'}).span.text
        time = page_bs.find('em',{ 'id':'dynamic-clock'}).text
        
        ind_code = 'bourcind'
        bource_ind = Index(code_to_name(ind_code), value, time, date_now)
        indexes['bourcind'] = bource_ind

        yield indexes,'Bource index\'s data gathering is finished'
    except Exception as e:
        yield indexes, 'In bource : '+str(e)
    
    browser.quit()
    
    #get gold world price
    try:
        headers = {
                'x-access-token': 'goldapi-4kzgtkvp8s6kt-io',
                'Content-Type': 'application/json'
                }
        data = requests.get(path.world_gold_url, headers=headers)     
        data= data.json()
        price = data['price']
        t = datetime.fromtimestamp(data['timestamp'])
        time = t.astimezone(timezone('Asia/Tehran')).time()
        ind_code = 'goldoz'
        name = 'اونس جهانی طلا'
        ind = Index(name, price, time, date_now)
        indexes[ind_code] = ind

        yield indexes,'World Gold\'s data gathering is finished'
    except Exception as e:
        yield indexes, 'In world gold : '+str(e)
               
    
    #get bitcoin price
    try:
        data = requests.get(path.bitcoin_url)

        price = str(data.json()['bitcoin']['usd'])
        name = 'بیت کوین'
        ind_code = 'btc'
        time = time_now

        ind = Index(name, price, time, date_now)
        indexes[ind_code] = ind
        yield indexes,'BitCoin\'s data gathering is finished'
    except Exception as e:
        yield indexes, 'In bitcoin : '+str(e)
    
    




