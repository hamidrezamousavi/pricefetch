from PIL import Image, ImageDraw, ImageFont
import arabic_reshaper
from bidi.algorithm import get_display
import jdatetime

from fileoperation import getDataOnFile
import path
from data import DateTime
from utilfunc import rialToToman, strDiff

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



def prepare_text(text):
    reshaped_text = arabic_reshaper.reshape(text)    
    bidi_text = get_display(reshaped_text)
    return bidi_text


def renderPage1():
    
    indexs_list = getDataOnFile(path.indexarchive)
    last_indexs = indexs_list[-1]
    prv_indexs = indexs_list[-2]
    img = Image.open(path.page1_tepl)
    d = ImageDraw.Draw(img)  
    
    font_header = ImageFont.truetype(path.BNAZANIN, 60)
    font_cur = ImageFont.truetype(path.BNAZANIN, 70)
    font_diff = ImageFont.truetype(path.BNAZANIN, 50)
    font_value = ImageFont.truetype(path.BNAZANIN, 70)
    
    xweekday =1020
    xday = 880
    xmonth = 780
    xyear = 680
    xhurlable = 450
    xhour = 300 
    yrow = 140
    date_time = DateTime()
    color = "#ffffff"
    text = prepare_text(date_time.weekday)
    d.text((xweekday, yrow), text, fill=color, anchor="rm", font=font_header)
    text = prepare_text(date_time.day)
    d.text((xday, yrow), text, fill=color, anchor="rm", font=font_header)
    text = prepare_text(date_time.month_str)
    d.text((xmonth, yrow), text, fill=color, anchor="rm", font=font_header)
    text = prepare_text(date_time.year)
    d.text((xyear, yrow), text, fill=color, anchor="rm", font=font_header)
    text = prepare_text("ساعت")
    d.text((xhurlable, yrow), text, fill=color, anchor="rm", font=font_header)
    text = prepare_text(date_time.hour+':'+date_time.minute)
    d.text((xhour, yrow), text, fill=color, anchor="rm", font=font_header)

    font_cur = ImageFont.truetype(path.BNAZANIN, 70)
    
    font_diff = ImageFont.truetype(path.BNAZANIN, 50)
    font_value = ImageFont.truetype(path.BNAZANIN, 70)
    
    xcur = 890
    xdiff = 540
    xval = 210
    yrow = 122
    dyrow = 130
    
    currency = ['dollar_rl','eur','aed','try','geram18',
                'sekee']

    for cur in currency:
        color = setColor()
        text = prepare_text(last_indexs[cur].name)
        d.text((xcur, yrow:=yrow+dyrow), text, fill=color, anchor="rm", font=font_cur)
        diff = strDiff(last_indexs[cur].value, prv_indexs[cur].value)
        diff = rialToToman(diff)
        text = prepare_text(diff)
        color = setColor(diff)
        d.text((xdiff, yrow), text, fill=color, anchor="mm", font=font_diff)
        text = prepare_text(rialToToman(last_indexs[cur].value))
        d.text((xval, yrow), text, fill=color, anchor="mm", font=font_value)


    xcur = 1050
    xdiff = 520
    xval = 200
    yrow = 900
    dyrow = 130
    
    currency = ['btc','bourcind']

    for cur in currency:
        color = setColor()
        text = prepare_text(last_indexs[cur].name)
        d.text((xcur, yrow:=yrow+dyrow), text, fill=color, anchor="rm", font=font_cur)
        diff = strDiff(last_indexs[cur].value, prv_indexs[cur].value)
        text = prepare_text(diff)
        color = setColor(diff)
        d.text((xdiff, yrow), text, fill=color, anchor="mm", font=font_diff)
        text = prepare_text(last_indexs[cur].value)
        d.text((xval, yrow), text, fill=color, anchor="mm", font=font_value)
                  
    
    img.save(path.page1)
    

def renderPage2():
    
    indexs_list = getDataOnFile(path.indexarchive)
    last_indexs = indexs_list[-1]
    prv_indexs = indexs_list[-2]
    img = Image.open(path.page2_tepl)
    d = ImageDraw.Draw(img)  
    
    indexs_list = getDataOnFile(path.indexarchive)
    last_indexs = indexs_list[-1]
    prv_indexs = indexs_list[-2]
    img = Image.open(path.page2_tepl)
    d = ImageDraw.Draw(img)  
    
    font_cr = ImageFont.truetype(path.BNAZANIN, 65)
    font_cr_s = ImageFont.truetype(path.BNAZANIN, 35)
    font_cn = ImageFont.truetype(path.BNAZANIN, 40)
    font_va = ImageFont.truetype(path.BNAZANIN, 75)
    xcr = 920
    ycr = -30
    xcu = xcr    
    ycu = ycr + 50
    xva = 700
    yva = 0
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
        text = prepare_text(rialToToman(last_indexs[cur].value))
        d.text((xva, yva:=yva+dy), text, fill=color, anchor="mm", font=font_va)
    
    #******************************
    xcr = 420
    ycr = -30
    xcu = xcr    
    ycu = ycr + 50
    xva = 180
    yva = 0
    dy = 125
    
   
    currency_col2 = ['rub','jpy','sek','azn','kwd','iqd','sar','myr']
    for cur in currency_col2:
        color = setColor()
        if cur == 'jpy':
            name = last_indexs[cur].name.split(' ')[0]
            text_yen = prepare_text(name[:2])
            text_100 = prepare_text(name[2:])
            d.text((xcr, ycr:=ycr+dy), text_yen, fill=color, anchor="rm", font=font_cr)
            d.text((xcr-55, ycr-5), text_100, fill=color, anchor="rm", font=font_cr_s)
        
        else:
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
        text = prepare_text(rialToToman(last_indexs[cur].value))
        d.text((xva, yva:=yva+dy), text, fill=color, anchor="mm", font=font_va)
    
    #**********once jahany*********
    color = setColor()
    text = prepare_text(last_indexs['goldoz'].name.split(' ')[0])
    d.text((1020, 1100), text, fill=color, anchor="rm", font=font_cr)
       
    try:
        text = prepare_text(last_indexs['goldoz'].name.split(' ')[1])
        d.text((1020, 1150), text, fill=color, anchor="rm", font=font_cn)
    except:
        pass
    diff = strDiff(last_indexs['goldoz'].value, prv_indexs['goldoz'].value)
    color = setColor(diff)
    text = prepare_text(last_indexs['goldoz'].value)
    d.text((700, 1125), text, fill=color, anchor="mm", font=font_va)
    
    

    #**************seke ghadim*****
    color = setColor()
    text = prepare_text(last_indexs['sekeb'].name.split(' ')[0])
    d.text((520, 1100), text, fill=color, anchor="rm", font=font_cr)
       
    try:
        text = prepare_text(last_indexs['sekeb'].name.split(' ')[1])
        d.text((520, 1150), text, fill=color, anchor="rm", font=font_cn)
    except:
        pass
    diff = strDiff(last_indexs['sekeb'].value, prv_indexs['sekeb'].value)
    color = setColor(diff)
    text = prepare_text(rialToToman(last_indexs['sekeb'].value))
    d.text((210, 1125), text, fill=color, anchor="mm", font=font_va)
    
    
    #**************seke nim*****
    color = setColor()
    text = prepare_text(last_indexs['nim'].name)
    d.text((1020, 1235), text, fill=color, anchor="rm", font=font_cr)
    diff = strDiff(last_indexs['nim'].value, prv_indexs['nim'].value)
    color = setColor(diff)
    text = prepare_text(rialToToman(last_indexs['nim'].value))
    d.text((700, 1235), text, fill=color, anchor="mm", font=font_va)
    

    #**************seke rob*****
    color = setColor()
    text = prepare_text(last_indexs['rob'].name)
    d.text((520, 1235), text, fill=color, anchor="rm", font=font_cr)
    diff = strDiff(last_indexs['rob'].value, prv_indexs['rob'].value)
    color = setColor(diff)
    text = prepare_text(rialToToman(last_indexs['rob'].value))
    d.text((210, 1235), text, fill=color, anchor="mm", font=font_va)


    
    
    img.save(path.page2)