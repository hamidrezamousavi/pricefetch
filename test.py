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
    
    font_cr = ImageFont.truetype(path.BNAZANIN, 38)
    font_cn = ImageFont.truetype(path.BNAZANIN, 24)
    font_va = ImageFont.truetype(path.BNAZANIN, 48)
    xcr = 590
    ycr = -40
    xcu = xcr    
    ycu = ycr + 30
    xva = 450
    yva = 40
    dy = 70
    
    currency = ['cad','aud','nzd','gbp','cny','inr','afn','thb','rub','jpy','sek','azn','kwd','iqd','sar','myr']
    for cur in currency:
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
    
    
    #img.save(path.page2)
    img.show()

renderPage2()