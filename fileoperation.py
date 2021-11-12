import json
from data import Index

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

    with open(filepath, 'r') as f_obj:
        try:#catch empty file exception 
            pervious_indexs = json.load(f_obj)
        except :
            pervious_indexs = []
    pervious_indexs.append(indexes)
    
    with open(filepath, 'w') as f_obj:
        json.dump(pervious_indexs, f_obj,cls=IndexEncoder)



def lastDataOnFile(filepath):
    with open(filepath, 'r') as f_obj:
        indexs_list = json.load(f_obj)
    for row in indexs_list:
        for item in row:
            for key in item:
                item[key] = decode_index(item[key])
    
    return indexs_list[-1][0]

