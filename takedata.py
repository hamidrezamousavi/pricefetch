from data import Index
from jdatetime import datetime
from fileoperation import saveDataOnFile
from path import indexarchive
import json 
with open('data1.csv','r') as f:
    data = json.load(f)    
indexs_list = []
for line in reversed(data):
    indexs = dict()
    indexs['dollar_rl'] = Index('دلار', line[0], line[9], datetime.strptime(line[8],'%Y-%m-%d').date())
    indexs['eur'] = Index('یورو', line[1], line[9], datetime.strptime(line[8],'%Y-%m-%d').date())
    indexs['aed'] = Index('درهم امارات', line[2], line[9], datetime.strptime(line[8],'%Y-%m-%d').date())
    indexs['try'] = Index('لیر ترکیه', line[3], line[9], datetime.strptime(line[8],'%Y-%m-%d').date())
    indexs['sekee'] = Index('سکه امامی', line[5], line[9], datetime.strptime(line[8],'%Y-%m-%d').date())
    indexs['geram18'] = Index('طلا(18)', line[4], line[9], datetime.strptime(line[8],'%Y-%m-%d').date())
    indexs['bourcind'] = Index('شاخص کل بورس', line[7], line[9], datetime.strptime(line[8],'%Y-%m-%d').date())
    indexs['btc'] = Index('بیت کوین', line[6], line[9], datetime.strptime(line[8],'%Y-%m-%d').date())
    indexs_list.append(indexs)
    saveDataOnFile(indexs,indexarchive)