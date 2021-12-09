from PIL import Image, ImageDraw, ImageFont
import arabic_reshaper
from bidi.algorithm import get_display
import jdatetime
from graph import makeChangeIcon, makeGraph, chooseArrow
from fileoperation import getDataOnFile
import path
from data import DateTime
from utilfunc import rialToToman, strDiff, strPercentage, addThousandSeperator

def setColor(diff = None):
    RED = "#ff0000"
    GREEN = "#00ff00"
    WHITE = "#ffffff"
    if diff == None:
        color = WHITE
    elif (diff == '0') or (diff == '0.00'):
        color = WHITE 
    elif diff.find('-')==0:
        color = "#ff0000"
    else:
        color = "#51ff5a"
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
    img.convert('RGBA')
    d = ImageDraw.Draw(img)  
    
    font_header = ImageFont.truetype(path.BNAZANIN, 60)
    font_cur_l = ImageFont.truetype(path.BNAZANIN, 70)
    font_cur_s = ImageFont.truetype(path.BNAZANIN, 50)
    font_diff = ImageFont.truetype(path.Oswald, 40)
    font_percent = ImageFont.truetype(path.Oswald, 50)
    font_value_l = ImageFont.truetype(path.Oswald, 80)
    font_value_s = ImageFont.truetype(path.Oswald, 60)
    
    color_header = '#FFC000'
    color_currency = '#FFC000'
    color_diff = "#ffffff"
    color_percent = "#ffffff"
    color_value = '#FFC000'
    
    
    
    #preper header
    xweekday =970
    xday = 770
    xmonth = 700
    xyear = 600
    xhurlable = 400
    xhour = 250 
    yrow = 100
    date_time = DateTime()
    color = color_header
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

    #preper table
    xcur = 1040
    xdiff = 710
    xpercent = 690
    xval = 450
    yrow = 75
    dydiff = -20
    dypercent = 30
    dyrow = 145
    xgraph = 10
    ygraph = 12
    xchange_icon = 580
    ychange_icon = 25
    graph_duration=180
    graph_dim = (270,150)
       
    currency = ['dollar_rl','eur','aed','try','geram18',
                'sekee','btc','bourcind']
    
    for cur in currency:
        if cur in ['geram18','sekee','btc','bourcind']:
            font_value = font_value_s
        else:
            font_value = font_value_l
        text = prepare_text(last_indexs[cur].name)
        
        if cur == 'bourcind':
            font_cur = font_cur_s
        else:
            font_cur = font_cur_l
        d.text((xcur, yrow:=yrow+dyrow), text, fill=color_currency, anchor="rm", font=font_cur)
        diff = strDiff(last_indexs[cur].value, prv_indexs[cur].value)
        
        change_icon = makeChangeIcon(diff)
        img.paste(change_icon,(xchange_icon,ychange_icon:=ychange_icon+dyrow),change_icon)      
         
        text = prepare_text(rialToToman(diff))
        d.text((xdiff, yrow+dydiff), text, fill=color_diff, anchor="mm", font=font_diff)
        
        precent = strPercentage(diff,last_indexs[cur].value)
        text = prepare_text(precent)
        d.text((xpercent, yrow+dypercent), text, fill=color_percent, anchor="mm", font=font_percent)
        if cur != 'btc':
            text = prepare_text(rialToToman(last_indexs[cur].value))
        else:
            #add dollar sing to btc value
            text = last_indexs[cur].value + u" \u0024" 
            text = prepare_text(text)
       
        d.text((xval, yrow), text, fill=color_value, anchor="mm", font=font_value)
        graph = makeGraph(cur, indexs_list, duration=graph_duration,graph_dim = graph_dim)
        img.paste(graph,(xgraph,ygraph:=ygraph+dyrow),mask= graph)
    
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
    
    color_currency = '#FFC000'
    color_value = '#FFC000'
    font_cr = ImageFont.truetype(path.BNAZANIN, 65)
    font_cr_s = ImageFont.truetype(path.BNAZANIN, 35)
    font_cn = ImageFont.truetype(path.BNAZANIN, 40)
    font_va = ImageFont.truetype(path.Oswald, 60)
    font_va_s = ImageFont.truetype(path.Oswald, 50)
    xcr = 920
    ycr = -30
    xcu = xcr    
    ycu = ycr + 50
    xva = 550
    yva = -20
    dy = 125
    xarrow = 750
    yarrow= -40
    currency_col1 = ['cad','aud','nzd','gbp','cny','inr','afn','thb',]
    
    for cur in currency_col1:
        text = prepare_text(last_indexs[cur].name.split(' ')[0])
        d.text((xcr, ycr:=ycr+dy), text, fill=color_currency, anchor="rm", font=font_cr)
        try:
            text = prepare_text(last_indexs[cur].name.split(' ')[1])
            d.text((xcu, ycu:=ycu+dy), text, fill=color_currency, anchor="rm", font=font_cn)
        except:
            text = prepare_text(last_indexs[cur].name.split(' ')[0])
            d.text((xcu, ycu:=ycu+dy), text, fill=color_currency, anchor="rm", font=font_cn)
        diff = strDiff(last_indexs[cur].value, prv_indexs[cur].value)
        arrow = chooseArrow(diff)
        img.paste(arrow,(xarrow,yarrow:=yarrow+dy),arrow)
        text = prepare_text(rialToToman(last_indexs[cur].value))
        d.text((xva, yva:=yva+dy), text, fill=color_value, anchor="lm", font=font_va)
    
    #******************************
    xcr = 420
    ycr = -30
    xcu = xcr    
    ycu = ycr + 50
    xva = 30
    yva = -20
    dy = 125
    xarrow = 225
    yarrow= -40
   
    currency_col2 = ['rub','jpy','sek','azn','kwd','iqd','sar','myr']
    for cur in currency_col2:
        color = setColor()
        if cur == 'jpy':
            name = last_indexs[cur].name.split(' ')[0]
            text_yen = prepare_text(name[:2])
            text_100 = prepare_text(name[2:])
            d.text((xcr, ycr:=ycr+dy), text_yen, fill=color_currency, anchor="rm", font=font_cr)
            d.text((xcr-55, ycr-5), text_100, fill=color_currency, anchor="rm", font=font_cr_s)
        
        else:
            text = prepare_text(last_indexs[cur].name.split(' ')[0])
            d.text((xcr, ycr:=ycr+dy), text, fill=color_currency, anchor="rm", font=font_cr)
        try:
            text = prepare_text(last_indexs[cur].name.split(' ')[1])
            d.text((xcu, ycu:=ycu+dy), text, fill=color_currency, anchor="rm", font=font_cn)
        except:
            text = prepare_text(last_indexs[cur].name.split(' ')[0])
            d.text((xcu, ycu:=ycu+dy), text, fill=color_currency, anchor="rm", font=font_cn)
        diff = strDiff(last_indexs[cur].value, prv_indexs[cur].value)
        arrow = chooseArrow(diff)
        img.paste(arrow,(xarrow,yarrow:=yarrow+dy),arrow)       
        text = prepare_text(rialToToman(last_indexs[cur].value))
        d.text((xva, yva:=yva+dy), text, fill=color_value, anchor="lm", font=font_va)
    
    #**********once jahany*********
    
    text = prepare_text(last_indexs['goldoz'].name.split(' ')[0])
    d.text((1020, 1100), text, fill=color_currency, anchor="rm", font=font_cr)
       
    try:
        text = prepare_text(last_indexs['goldoz'].name.split(' ')[1])
        d.text((1020, 1150), text, fill=color_currency, anchor="rm", font=font_cn)
    except:
        pass
    diff = strDiff(last_indexs['goldoz'].value, prv_indexs['goldoz'].value) 
    arrow = chooseArrow(diff)
    img.paste(arrow,(800,1100),arrow)
    text = prepare_text(last_indexs['goldoz'].value+ u" \u0024")
    d.text((550, 1125), text, fill=color_value, anchor="lm", font=font_va)
    
   
    #**************seke ghadim*****
   
    text = prepare_text(last_indexs['sekeb'].name.split(' ')[0])
    d.text((520, 1100), text, fill=color_currency, anchor="rm", font=font_cr)  
    try:
        text = prepare_text(last_indexs['sekeb'].name.split(' ')[1])
        d.text((520, 1150), text, fill=color_currency, anchor="rm", font=font_cn)
    except:
        pass
    diff = strDiff(last_indexs['sekeb'].value, prv_indexs['sekeb'].value)
    arrow = chooseArrow(diff)
    img.paste(arrow,(300,1100),arrow)
    text = prepare_text(rialToToman(last_indexs['sekeb'].value))
    d.text((30, 1125), text, fill=color_value, anchor="lm", font=font_va_s)
    
    
    #**************seke nim*****
    
    text = prepare_text(last_indexs['nim'].name.split(' ')[0])
    d.text((1020, 1235), text, fill=color_currency, anchor="rm", font=font_cr)  
    try:
        text = prepare_text(last_indexs['nim'].name.split(' ')[1])
        d.text((1020, 1285), text, fill=color_currency, anchor="rm", font=font_cn)
    except:
        pass

    #text = prepare_text(last_indexs['nim'].name)
    #d.text((1020, 1235), text, fill=color_currency, anchor="rm", font=font_cr)
    diff = strDiff(last_indexs['nim'].value, prv_indexs['nim'].value)
    arrow = chooseArrow(diff)
    img.paste(arrow,(800,1225),arrow)
    text = prepare_text(rialToToman(last_indexs['nim'].value))
    d.text((550, 1260), text, fill=color_value, anchor="lm", font=font_va_s)
    

    #**************seke rob*****
    
    text = prepare_text(last_indexs['rob'].name.split(' ')[0])
    d.text((520, 1235), text, fill=color_currency, anchor="rm", font=font_cr)  
    try:
        text = prepare_text(last_indexs['rob'].name.split(' ')[1])
        d.text((520, 1285), text, fill=color_currency, anchor="rm", font=font_cn)
    except:
        pass
    #text = prepare_text(last_indexs['rob'].name)
    #d.text((520, 1235), text, fill=color_currency, anchor="rm", font=font_cr)
    diff = strDiff(last_indexs['rob'].value, prv_indexs['rob'].value)
    arrow = chooseArrow(diff)
    img.paste(arrow,(300,1225),arrow)
    text = prepare_text(rialToToman(last_indexs['rob'].value))
    d.text((30, 1260), text, fill=color_value, anchor="lm", font=font_va_s)
    img.save(path.page2)

