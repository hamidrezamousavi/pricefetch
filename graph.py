
from jdatetime import date
from PIL import Image, ImageDraw,ImageFont
from fileoperation import getDataOnFile
from utilfunc import getIndexHistory
import path

def makeGraph(index_code, indexs_list, duration=180,graph_dim = (270,137)):
    graph_x = graph_dim[0]
    graph_y = graph_dim[1]
    low_margin = 25
    upper_margin = 25
    today = date.today()
    currency_history = getIndexHistory(index_code,indexs_list, duration)
    
    points = {x:0 for x in range(graph_x)}
    
   #find x cordination for points
    max = currency_history.max_day_distance
    min = currency_history.min_day_distance
    scale_factor = graph_x/(max-min)
    for item in currency_history.data:
        x = graph_x-int(scale_factor*(today-item[1]).days-min)
        points[x] = int(item[0])
        
    
    

    
    #make data for points that have not value
    for i in range(graph_x):
        if points[i] == 0:
            for j in range(i,graph_x+1):
                if points[j] != 0:
                    
                    x = (points[j]-points[i-1])/(j-(i-1))
                    for p in range(i,j):
                        points[p]=points[p-1]+x
                    break
    
    #find y cordination for points
    y_scale_factor = (graph_y - (low_margin + upper_margin))/(currency_history.max_value - currency_history.min_value)
    for key in points:
        points[key] = (points[key]- currency_history.min_value) * y_scale_factor
        points[key] = graph_y - low_margin -points[key]
   
     
    

    graph = Image.new('RGBA',size=(graph_x,graph_y),color=(255,255,255,0))
    draw = ImageDraw.Draw(graph)
    low_margin_position = graph_y -low_margin
    previous_point = (0,low_margin_position)
    for point in points:
        draw.line(((previous_point),(point,points[point])),width=2,joint='curve',fill ='#97DDF6')
        previous_point = (point,points[point])
    
   # draw.line(((0,low_margin_position),(graph_x,low_margin_position)),width=3,)
   # draw.line(((0, upper_margin ),(graph_x,upper_margin)),width=3)
    
    limit_font = ImageFont.truetype(path.Oswald,40) 
    limit_color = '#FFBF00'
    if index_code!='btc':
        min_limit = str(int(currency_history.min_value/10))
        max_limit = str(int(currency_history.max_value/10))
    else:
        min_limit = str(f'{currency_history.min_value:1.0f}')
        max_limit = str(f'{currency_history.max_value:1.0f}')

    draw.text((0,low_margin_position),text=min_limit,fill = limit_color,font = limit_font,anchor="lm" )
    draw.text((0,upper_margin),text=max_limit,fill = limit_color,font = limit_font,anchor="lm" )
    
    return graph


def makeChangeIcon(diff = None):
    
    if diff == None:
        change_icon = Image.open(path.red_change).convert('RGBA')
    elif (diff == '0') or (diff == '0.00'):
        change_icon = Image.open(path.green_change).convert('RGBA')
    elif diff.find('-')==0:
        change_icon = Image.open(path.red_change).convert('RGBA')
    else:
        change_icon = Image.open(path.green_change).convert('RGBA')
    return change_icon




if __name__ == '__main__':
    indexs_list = getDataOnFile(path.indexarchive)
    graph = makeGraph('dollar_rl',indexs_list,duration=180)
    graph.show()