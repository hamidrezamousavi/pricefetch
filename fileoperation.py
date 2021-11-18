import json
from data import Index, DateTime

class IndexEncoder(json.JSONEncoder):
    #define how index object conver to dict
    def default(self, data):
        if isinstance(data, Index):
            return dict(name = data.name,
                        value= data.value,
                        time= data.time)
        else:
            return super().default(data)

def decode_index(data):
    #make index from dict
    return Index(data['name'],data['value'],data['time'])

def saveDataOnFile(indexes,filepath):

    with open(filepath, 'r',encoding="utf8") as f_obj:
        try:#catch empty file exception 
            pervious_indexs = json.load(f_obj)
        except :
            pervious_indexs = []
    pervious_indexs.append(indexes)
   
    with open(filepath, 'w',encoding="utf8") as f_obj:
        json.dump(pervious_indexs, f_obj,cls=IndexEncoder, ensure_ascii=False)



def getDataOnFile(filepath):
    with open(filepath, 'r',encoding="utf8") as f_obj:
        indexs_list = json.load(f_obj)
    
    for index in indexs_list:
        for key in index:
            index[key] = decode_index(index[key])
    
    return indexs_list

def fileName():
    file_name = DateTime.month + DateTime.day + DateTime.hour +DateTime.minute
    return file_name
