from typing import Iterator, List
from flask import Flask, render_template, request, send_file
import requests
from datetime import datetime
from pytz import timezone
from data import Index, code_to_name
from bs4 import BeautifulSoup, Tag
from fileoperation import saveDataOnFile, lastDataOnFile    
#import tgju
def foo():
          
    indexes = dict()
   
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
    

def save_form(formrequest, indexes):
    #this block update indexes based on form manual changes 
    #because request.form return multidict value and time have same key
    #so in every for loop first value is catch then invoke next funtion 
    # to catch time
    request_itarator = formrequest.items(multi=True)
    for key, value in request_itarator:
        if key in indexes:
            indexes[key].value = value
            b = next(request_itarator)
            indexes[key].time = b[1]
    
    saveDataOnFile(indexes,'numbers.json')
    return indexes

too = foo()
indexes = dict()
message = list()
app = Flask(__name__)

@app.route('/',methods = ['GET', 'POST'])
def index():
    global too
    global indexes   
    if request.method == "POST":
        
        if request.form.get("save"):
            save_form(request.form, indexes)
            return render_template('resualt.html',message = message, indexes = indexes)
                        
        else:    
            try:
                indexes,msg = next(too)
                message.append(msg)
            except ValueError as err:
                print(err)
            except StopIteration:
                # preper new get_data genetator for next fetch request
                too = foo()
                return render_template('resualt.html',message = message, indexes = indexes)
            return render_template('post.html',message = message )

    message.clear()
    return render_template('index.html')

@app.route('/download')
def download():
    return send_file( path_or_file='todo.txt',as_attachment=True,download_name='d1.txt')

   


if __name__=="__main__":
    app.run()