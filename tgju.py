from urllib.request import urlopen
from urllib.error import HTTPError, URLError

from bs4 import BeautifulSoup

from data import currency, code_to_name

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
    page = urlopen('https://www.tgju.org/currency')
    currencies = dict()

    page_bs = BeautifulSoup(page,'html.parser')

    price_table = page_bs.find_all('table',{'data-tab-id':"1"})

    print('-'*50)
    for table in price_table:
        for table_row in table.tbody.children:
            if type(table_row)== type(table):
                cur_code = table_row.get_attribute_list('data-market-row')[0].partition('_')[2]
                cur = currency(code_to_name(cur_code),
                                table_row.td.get_text(),
                                table_row.find_all('td')[4].get_text()
                                )
                currencies[cur_code] = cur

    return currencies
data = get_data()

for key, value in data.items():
    print(f'cur {value.name} code is {key} and price is{value.value} and time{value.time}')

