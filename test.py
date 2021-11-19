from PIL import Image, ImageDraw, ImageFont, ImageFilter
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
    color = "#ffffff"
    text = prepare_text(DateTime.weekday)
    d.text((xweekday, yrow), text, fill=color, anchor="rm", font=font_header)
    text = prepare_text(DateTime.day)
    d.text((xday, yrow), text, fill=color, anchor="rm", font=font_header)
    text = prepare_text(DateTime.month_str)
    d.text((xmonth, yrow), text, fill=color, anchor="rm", font=font_header)
    text = prepare_text(DateTime.year)
    d.text((xyear, yrow), text, fill=color, anchor="rm", font=font_header)
    text = prepare_text("ساعت")
    d.text((xhurlable, yrow), text, fill=color, anchor="rm", font=font_header)
    text = prepare_text(DateTime.hour+':'+DateTime.minute)
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
        text = prepare_text(diff)
        color = setColor(diff)
        d.text((xdiff, yrow), text, fill=color, anchor="mm", font=font_diff)
        text = prepare_text(last_indexs[cur].value)
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
    
    #img.save(path.page1)
    
    
    

    img.show()
    img = img.filter(ImageFilter.SHARPEN)
    img.show()
    img = img.filter(ImageFilter.SHARPEN)
    img.show()

renderPage1()
