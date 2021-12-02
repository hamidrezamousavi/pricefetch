
from data import History
from fileoperation import getDataOnFile
import path
from jdatetime import date
from PIL import Image, ImageDraw
indexs_list = getDataOnFile(path.indexarchive)



def getIndexHistory(index_code, indexs_list, duration):
    
    #base_date = date.today() - timedelta(days=duration)
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
        
    #find y cordination for points
    for point, value in points.items():
        if value != 0:
            print(point,value)

    
    #make data for points that have not value
    for i in range(graph_x):
        if points[i] == 0:
            for j in range(i,graph_x+1):
                if points[j] != 0:
                    
                    x = (points[j]-points[i-1])/(j-(i-1))
                    for p in range(i,j):
                        points[p]=points[p-1]+x
                    break
    
    y_scale_factor = (graph_y - (low_margin + upper_margin))/(currency_history.max_value - currency_history.min_value)
    
    for key in points:
        points[key] = (points[key]- currency_history.min_value) * y_scale_factor
        points[key] = graph_y - low_margin -points[key]
   
    print(currency_history.data)
    print(points)
    
    graph = Image.new('RGBA',size=(graph_x,graph_y),color=(100,10,200,30))
    draw = ImageDraw.Draw(graph)
    for point in points:
        print(point,points[point])
        draw.point((point,points[point]))

    upper_margin
    low_margin_position = graph_y -low_margin
    draw.line(((0,low_margin_position),(270,low_margin_position)))
    draw.line(((0, upper_margin ),(270,upper_margin)))
    graph.show()

makeGraph('dollar_rl',indexs_list,duration=180)
