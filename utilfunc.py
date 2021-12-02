import math
from jdatetime import date
from data import History

def strDiff(str1, str2):
    try:
        str1=str1.replace(',','')
        str2=str2.replace(',','')
        try:
            str1 = int(str1)
        except ValueError:
            str1 = float(str1)
        try:
            str2 = int(str2)
        except ValueError:
            str2 = float(str2)
        resualt = str1 - str2
    except:
        return None
    if isinstance(resualt,float):
        resualt = f'{resualt:0.2f}'
    return str(resualt)


def rialToToman(number:str)->str:
    periodpos = number.find('.')
    periodpos = len(number) if periodpos == -1 else periodpos
    number = number.replace('.','')
    number = number[:periodpos-1]+'.'+number[periodpos-1:]
    number = number.replace(',','')
    periodpos = number.find('.')
    cunter = -1
    cunter_start = False
    num = ''
    for chr in reversed(number):
        if chr == '.':
            cunter_start = True
        if cunter_start:
            cunter = cunter + 1
        if cunter and math.remainder(cunter, 3)  == 0 :
            num = num+chr + ','
        else:
            num = num + chr
       
    number = num[::-1]
    if number.find(',') == 0:
        number = number[1:]
   
    periodpos = number.find('.') 
    if number[periodpos+1] == '0':
        number = number[:periodpos] 
    if number ==  '':
        number = '0' 
    return number


def getIndexHistory(index_code, indexs_list, duration=180):
    
    #base_date = date.today() - timedelta(days=duration)
    today = date.today()
    history = History()
    temp = date(1,1,1)
    
    for indexs in indexs_list[::-1]:
        if (today - indexs[index_code].date).days <= duration:
            history.max =  indexs[index_code].value if int(indexs[index_code].value) > int(history.max) else history.max
            history.min =  indexs[index_code].value if int(indexs[index_code].value) < int(history.min) or history.min == '0' else history.min
            #select one record for each days
            if (temp - indexs[index_code].date).days != 0:
                history.data=((indexs[index_code].value,indexs[index_code].date))   
                temp = indexs[index_code].date
                history.days += 1
        else:
            break    
       
    return history


