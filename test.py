from PIL import Image, ImageDraw, ImageFont
import arabic_reshaper
from bidi.algorithm import get_display
import jdatetime

from fileoperation import getDataOnFile
import path
from data import DateTime


def setColor(diff = None):
    RED = "#ff0000"
    GREEN = "#00ff00"
    WHITE = "#ffffff"
    if diff == None:
        color = WHITE
    elif (diff == '0') or (diff == '0.00'):
        color = WHITE 
    elif diff.find('-')==0:
        color = RED
    else:
        color = GREEN
    return color


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


def prepare_text(text):
    reshaped_text = arabic_reshaper.reshape(text)    
    bidi_text = get_display(reshaped_text)
    return bidi_text


    

def renderPage2():
    
    indexs_list = getDataOnFile(path.indexarchive)
    last_indexs = indexs_list[-1]
    prv_indexs = indexs_list[-2]
    img = Image.open(path.page2_tepl)
    d = ImageDraw.Draw(img)  
    
    font_cr = ImageFont.truetype(path.BNAZANIN, 65)
    font_cn = ImageFont.truetype(path.BNAZANIN, 40)
    font_va = ImageFont.truetype(path.BNAZANIN, 75)
    xcr = 920
    ycr = -30
    xcu = xcr    
    ycu = ycr + 50
    xva = 700
    yva = 10
    dy = 125
    
    currency_col1 = ['cad','aud','nzd','gbp','cny','inr','afn','thb',]
    
    for cur in currency_col1:
        color = setColor()
        text = prepare_text(last_indexs[cur].name.split(' ')[0])
        d.text((xcr, ycr:=ycr+dy), text, fill=color, anchor="rm", font=font_cr)
        try:
            text = prepare_text(last_indexs[cur].name.split(' ')[1])
            d.text((xcu, ycu:=ycu+dy), text, fill=color, anchor="rm", font=font_cn)
        except:
            text = prepare_text(last_indexs[cur].name.split(' ')[0])
            d.text((xcu, ycu:=ycu+dy), text, fill=color, anchor="rm", font=font_cn)
        diff = strDiff(last_indexs[cur].value, prv_indexs[cur].value)
        color = setColor(diff)
        text = prepare_text(last_indexs[cur].value)
        d.text((xva, yva:=yva+dy), text, fill=color, anchor="mm", font=font_va)
    
    #******************************
    xcr = 420
    ycr = -30
    xcu = xcr    
    ycu = ycr + 50
    xva = 200
    yva = 10
    dy = 125
    
   
    currency_col2 = ['rub','jpy','sek','azn','kwd','iqd','sar','myr']
    for cur in currency_col2:
        color = setColor()
        text = prepare_text(last_indexs[cur].name.split(' ')[0])
        d.text((xcr, ycr:=ycr+dy), text, fill=color, anchor="rm", font=font_cr)
        try:
            text = prepare_text(last_indexs[cur].name.split(' ')[1])
            d.text((xcu, ycu:=ycu+dy), text, fill=color, anchor="rm", font=font_cn)
        except:
            text = prepare_text(last_indexs[cur].name.split(' ')[0])
            d.text((xcu, ycu:=ycu+dy), text, fill=color, anchor="rm", font=font_cn)
        diff = strDiff(last_indexs[cur].value, prv_indexs[cur].value)
        color = setColor(diff)
        text = prepare_text(last_indexs[cur].value)
        d.text((xva, yva:=yva+dy), text, fill=color, anchor="mm", font=font_va)
    
    #**********once jahany*********
    color = setColor()
    text = prepare_text(last_indexs['goldoz'].name.split(' ')[0])
    d.text((1000, 1100), text, fill=color, anchor="rm", font=font_cr)
       
    try:
        text = prepare_text(last_indexs['goldoz'].name.split(' ')[1])
        d.text((1000, 1150), text, fill=color, anchor="rm", font=font_cn)
    except:
        text = prepare_text(last_indexs['goldoz'].name.split(' ')[0])
        d.text((1000, 1150), text, fill=color, anchor="rm", font=font_cn)
    diff = strDiff(last_indexs['goldoz'].value, prv_indexs['goldoz'].value)
    color = setColor(diff)
    text = prepare_text(last_indexs['goldoz'].value)
    d.text((700, 1125), text, fill=color, anchor="mm", font=font_va)
    
    

    #**************seke ghadim*****
    color = setColor()
    text = prepare_text(last_indexs['sekeb'].name.split(' ')[0])
    d.text((500, 1100), text, fill=color, anchor="rm", font=font_cr)
       
    try:
        text = prepare_text(last_indexs['sekeb'].name.split(' ')[1])
        d.text((500, 1150), text, fill=color, anchor="rm", font=font_cn)
    except:
        text = prepare_text(last_indexs['sekeb'].name.split(' ')[0])
        d.text((500, 1150), text, fill=color, anchor="rm", font=font_cn)
    diff = strDiff(last_indexs['sekeb'].value, prv_indexs['sekeb'].value)
    color = setColor(diff)
    text = prepare_text(last_indexs['sekeb'].value)
    d.text((250, 1125), text, fill=color, anchor="mm", font=font_va)
    
    
    #**************seke nim*****
    color = setColor()
    text = prepare_text(last_indexs['nim'].name)
    d.text((1000, 1235), text, fill=color, anchor="rm", font=font_cr)
    diff = strDiff(last_indexs['nim'].value, prv_indexs['nim'].value)
    color = setColor(diff)
    text = prepare_text(last_indexs['nim'].value)
    d.text((700, 1235), text, fill=color, anchor="mm", font=font_va)
    

    #**************seke rob*****
    color = setColor()
    text = prepare_text(last_indexs['rob'].name)
    d.text((500, 1235), text, fill=color, anchor="rm", font=font_cr)
    diff = strDiff(last_indexs['rob'].value, prv_indexs['rob'].value)
    color = setColor(diff)
    text = prepare_text(last_indexs['rob'].value)
    d.text((250, 1235), text, fill=color, anchor="mm", font=font_va)

    #img.save(path.page2)
    img.show()

renderPage2()