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


def renderPage1():
    
    indexs_list = getDataOnFile(path.indexarchive)
    last_indexs = indexs_list[-1]
    prv_indexs = indexs_list[-2]
    img = Image.open(path.page1_tepl)
    d = ImageDraw.Draw(img)  
    
    color = "#ffffff"
    font = ImageFont.truetype(path.BNAZANIN, 30)
    text = prepare_text(DateTime.weekday)
    d.text((740, 20), text, fill=color, anchor="rm", font=font)
    text = prepare_text(DateTime.day)
    d.text((600, 20), text, fill=color, anchor="rm", font=font)
    text = prepare_text(DateTime.month)
    d.text((550, 20), text, fill=color, anchor="rm", font=font)
    text = prepare_text(DateTime.year)
    d.text((500, 20), text, fill=color, anchor="rm", font=font)
    text = prepare_text(DateTime.hour+':'+DateTime.minute)
    d.text((100, 20), text, fill=color, anchor="rm", font=font)

    color = setColor()
    font = ImageFont.truetype(path.BNAZANIN, 48)
    text = prepare_text(last_indexs['dollar_rl'].name)
    d.text((620, 90), text, fill=color, anchor="rm", font=font)
    
    diff = strDiff(last_indexs['dollar_rl'].value, prv_indexs['dollar_rl'].value)
    text = prepare_text(diff)
        
    color = setColor(diff)
    d.text((370, 90), text, fill=color, anchor="mm", font=font)
    text = prepare_text(last_indexs['dollar_rl'].value)
    d.text((170, 90), text, fill=color, anchor="mm", font=font)
    
    #******************************
    color = setColor()
    font = ImageFont.truetype(path.BNAZANIN, 48)
    text = prepare_text(last_indexs['eur'].name)
    d.text((620, 160), text, fill=color, anchor="rm", font=font)
    
    diff = strDiff(last_indexs['eur'].value, prv_indexs['eur'].value)
    text = prepare_text(diff)
        
    color = setColor(diff)
    d.text((370, 160), text, fill=color, anchor="mm", font=font)
    text = prepare_text(last_indexs['eur'].value)
    d.text((170, 160), text, fill=color, anchor="mm", font=font)
    
#******************************
    color = setColor()
    font = ImageFont.truetype(path.BNAZANIN, 48)
    text = prepare_text(last_indexs['aed'].name)
    d.text((620, 240), text, fill=color, anchor="rm", font=font)
    
    diff = strDiff(last_indexs['aed'].value, prv_indexs['aed'].value)
    text = prepare_text(diff)
        
    color = setColor(diff)
    d.text((370, 240), text, fill=color, anchor="mm", font=font)
    text = prepare_text(last_indexs['aed'].value)
    d.text((170, 240), text, fill=color, anchor="mm", font=font)

#******************************
    color = setColor()
    font = ImageFont.truetype(path.BNAZANIN, 48)
    text = prepare_text(last_indexs['try'].name)
    d.text((620, 320), text, fill=color, anchor="rm", font=font)
    
    diff = strDiff(last_indexs['try'].value, prv_indexs['try'].value)
    text = prepare_text(diff)
        
    color = setColor(diff)
    d.text((370, 320), text, fill=color, anchor="mm", font=font)
    text = prepare_text(last_indexs['try'].value)
    d.text((170, 320), text, fill=color, anchor="mm", font=font)
    
#******************************
    color = setColor()
    font = ImageFont.truetype(path.BNAZANIN, 42)
    text = prepare_text(last_indexs['geram18'].name)
    d.text((620, 400), text, fill=color, anchor="rm", font=font)
    
    diff = strDiff(last_indexs['geram18'].value, prv_indexs['geram18'].value)
    text = prepare_text(diff)
        
    color = setColor(diff)
    d.text((370, 400), text, fill=color, anchor="mm", font=font)
    text = prepare_text(last_indexs['geram18'].value)
    d.text((170, 400), text, fill=color, anchor="mm", font=font)
       
    
#******************************
    color = setColor()
    font = ImageFont.truetype(path.BNAZANIN, 42)
    text = prepare_text(last_indexs['sekee'].name)
    d.text((620, 480), text, fill=color, anchor="rm", font=font)
    
    diff = strDiff(last_indexs['sekee'].value, prv_indexs['sekee'].value)
    text = prepare_text(diff)
        
    color = setColor(diff)
    d.text((370, 480), text, fill=color, anchor="mm", font=font)
    text = prepare_text(last_indexs['sekee'].value)
    d.text((170, 480), text, fill=color, anchor="mm", font=font)
        
#******************************
    color = setColor()
    font = ImageFont.truetype(path.BNAZANIN, 42)
    text = prepare_text(last_indexs['btc'].name)
    d.text((620, 560), text, fill=color, anchor="rm", font=font)
    
    diff = strDiff(last_indexs['btc'].value, prv_indexs['btc'].value)
    text = prepare_text(diff)
        
    color = setColor(diff)
    d.text((370, 560), text, fill=color, anchor="mm", font=font)
    text = prepare_text(last_indexs['btc'].value)
    d.text((170, 560), text, fill=color, anchor="mm", font=font)
#******************************
    color = setColor()
    font = ImageFont.truetype(path.BNAZANIN, 42)
    text = prepare_text(last_indexs['bourcind'].name)
    d.text((700, 640), text, fill=color, anchor="rm", font=font)
    
    diff = strDiff(last_indexs['bourcind'].value, prv_indexs['bourcind'].value)
    text = prepare_text(diff)
        
    color = setColor(diff)
    d.text((370, 640), text, fill=color, anchor="mm", font=font)
    text = prepare_text(last_indexs['bourcind'].value)
    d.text((170, 640), text, fill=color, anchor="mm", font=font)
                  
    
    img.save(path.page1)
    #img.show()




#font = ImageFont.truetype(font_path, size=600)
#draw = ImageDraw.Draw(img)
#width_text, height_text = draw.textsize(text, font)
#
#offset_x, offset_y = font.getoffset(text)
#width_text += offset_x