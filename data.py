

class Index:
    def __init__(self,name:str, value:str, time:str) -> None:
        self._name = name
        self._value = value
        self._time = time
    
   
    @property
    def name(self):
        return self._name
   
    @name.setter
    def name(self,name):
        self._name = name

    @name.getter
    def name(self):
        return self._name

   
    @property
    def value(self):
        return self._value
   
    @value.setter
    def value(self,value):
        self._value = value

    @value.getter
    def value(self):
        return self._value

    @property
    def time(self):
        return self._time
   
    @time.setter
    def time(self,time):
        self._time = time

    @time.getter
    def time(self):
        return self._time


def code_to_name(code):
   
    name = {
            'dollar_rl':'دلار',
            'eur':'یورو',
            'gbp':'پوند',
            'aed':'درهم امارات',
            'try':'لیر ترکیه',
            'cny':'یوان چین',
            'jpy':' ( 100 ین )ین ژاپن',
            'cad':'دلار کانادا',
            'aud':'دلار استرالیا',
            'nzd':'دلار نیوزیلند',
            'chf':'فرانک سوئیس',
            'afn':'افغانی',
            'sek':'کرون سوئد',
    	    'rub':'روبل روسیه',
            'azn':'منات آذربایجان',
            'amd':'درام ارمنستان',
            'kwd':'دینار کویت',
            'sar':'ریال عربستان',
            'qar':'ریال قطر',
            'omr':'ریال عمان',
            'gel':'لاری گرجستان',
            'iqd':'دینار عراق',
            'bhd':'دینار بحرین',
            'syp':'لیر سوریه(10لیر)',
            'dkk':'کرون دانمارک',
            'nok':'کرون نروژ',
            'inr':'روپیه هند',
            'pkr':'روپیه پاکستان',
            'sgd':'دلار سنگاپور',
            'hkd':'دلار هنگ کنگ',
            'myr':'رینگیت مالزی',
            'thb':'بات تایلند',
             }
     
    return name.setdefault(code) 

