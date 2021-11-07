from urllib.request import urlopen
from urllib.error import HTTPError, URLError

from bs4 import BeautifulSoup, Tag

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

    #get currency data
    page = urlopen('https://www.tgju.org/currency')
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

    #get gold data
    

    

    return indexes




data = get_data()

for key, value in data.items():
    print(f'cur {value.name} code is {key} and price is{value.value} and time{value.time}')

