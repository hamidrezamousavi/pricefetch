from flask import Flask, render_template, request, send_file
import requests
from datetime import datetime
from pytz import timezone
from bs4 import BeautifulSoup, Tag

from data import initTotalIndexs
from tgju import get_data
from fileoperation import fileName, saveDataOnFile   
from render import renderPage1  
import path
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
    
    saveDataOnFile(indexes,path.indexarchive)
    return indexes

get_data_iterator = get_data()
total_indexs = initTotalIndexs()
indexes = dict()
message = list()
app = Flask(__name__)

@app.route('/',methods = ['GET', 'POST'])
def index():
    global get_data_iterator
    global indexes   
    if request.method == "POST":
        
        if request.form.get("save"):
            save_form(request.form, total_indexs)
            return render_template(path.resualt_html,message = message, indexes = total_indexs)
                        
        else:    
            try:
                indexes,msg = next(get_data_iterator)
                message.append(msg)
            except ValueError as err:
                print(err)
            except StopIteration:
                # preper new get_data genetator for next fetch request
                get_data_iterator = get_data()
                #because it possible some index dont gather so with total index trace wanted index 
                total_indexs.update(indexes)
                return render_template(path.resualt_html,message = message, indexes = total_indexs)
            return render_template(path.post_html,message = message )

    message.clear()
    return render_template(path.index_html)

@app.route('/download1')
def download1():
    renderPage1()
    file_name = fileName() +'_1.jpg' 
    return send_file( path_or_file=path.page1,as_attachment=True,download_name=file_name)
@app.route('/download2')
def download2():
    return send_file( path_or_file='todo.txt',as_attachment=True,download_name='d2.txt')

   


if __name__=="__main__":
    app.run()