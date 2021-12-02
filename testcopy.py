
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
            history.min_value =  value if value < history.min_value or history.min_value == 0 else history.min_value
            history.min_day_distance = distance if distance < history.min_day_distance or  history.min_day_distance == 0  else history.min_day_distance
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

    print(currency_history.data)
    
   # graph = Image.new('RGBA',size=(graph_x,graph_y),color=(10,10,200,255))
   # draw = ImageDraw.Draw(graph)
   # for i in range(100):
   #     draw.point((i,i))
   # graph.show()

makeGraph('dollar_rl',indexs_list,duration=700)
