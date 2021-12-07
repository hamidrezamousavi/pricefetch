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

def strPercentage(str1, str2):
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
        resualt = (str1/str2)*100
    except:
        return None
    if isinstance(resualt,float):
        resualt = f'%{resualt:0.1f}'
    return str(resualt)

def rialToToman(number:str)->str:
    sing = True
    if number.find('-') == 0:
        sing = False
        number = number.replace('-','')
        
    if number.find('.')==0:
        number = '0'+number
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
    
    if number.find(',') == 0 :
        number = number[1:]
   
    periodpos = number.find('.') 
    #if number[periodpos+1] == '0':
    #    number = number[:periodpos] 
    if sing == False:
        number = '-' + number
    if number ==  '':
        number = '0' 
    return number

def addThousandSeperator(str):
    resualt = ''
    decim = ''
    if str.find('.')!= -1:
        str,decim = str.split('.')
    i = 0
    for chr in reversed(str):
        
        if i%3 == 0 and  i>=3:
            resualt = resualt+','+chr
        else:
            resualt = resualt + chr    
        i += 1
    resualt = resualt[::-1]
    if decim:
        resualt = resualt + '.'+decim
    return resualt
    
def getIndexHistory(index_code, indexs_list, duration):
    
    today = date.today()
    history = History()
    temp = date(1,1,1)
    
    for indexs in indexs_list[::-1]:
        distance = (today - indexs[index_code].date).days
        if distance <= duration:
            value = float(indexs[index_code].value.replace(',',''))
            history.max_value =  value if value > history.max_value else history.max_value
            history.min_value =  value if value < history.min_value or history.min_value == -1 else history.min_value
            history.min_day_distance = distance if distance < history.min_day_distance or  history.min_day_distance == -1  else history.min_day_distance
            history.max_day_distance = distance if distance > history.max_day_distance  else history.max_day_distance
            
            if (temp - indexs[index_code].date).days != 0:
                history.data=((value,indexs[index_code].date))   
                temp = indexs[index_code].date
                history.days += 1
        else:
            break    
    

    return history

