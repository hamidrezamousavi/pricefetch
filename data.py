import jdatetime
from pytz import timezone

request_indx = {
            'dollar_rl':'دلار',
            'eur':'یورو',
            'gbp':'پوند انگلیس',
            'aed':'درهم امارات',
            'try':'لیر ترکیه',
            'cny':'یوان چین',
            'jpy':'ین(100) ژاپن',
            'cad':'دلار کانادا',
            'aud':'دلار استرالیا',
            'nzd':'دلار نیوزیلند',
            'chf':'فرانک سوئیس',
            'afn':'افغانی افغانستان',
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
            'sekee':'سکه امامی',
            'sekeb':'سکه بهار آزادی',
            'nim':'نیم سکه',
            'rob':'ربع سکه',
            'gerami':'سکه گرمی',
            'geram18':'طلا(18) ',
            'gold_740k':'طلای 18 عیار 740',
            'geram24':'طلای ۲۴ عیار',
            'gold_mini_size':'طلای دست دوم',
            'goldoz':'اونس جهانیطلا',
            'bourcind':'شاخص کل بورس',
            'btc':'بیت کوین',
             }

months = {
        '01':'فروردین',
        '02':'اردیبهشت',
        '03':'خرداد',
        '04':'تیر',
        '05':'مرداد',
        '06':'شهریور',
        '07':'مهر',
        '08':'آبان',
        '09':'آذر',
        '10':'دی',
        '11':'بهمن',
        '12':'اسفند',
        }
weekdays = {
        'Sat':'شنبه',
        'Sun':'یکشنبه',
        'Mon':'دوشنبه',
        'Tue':'سه شنبه',
        'Wed':'چهارشنبه',
        'Thu':'پنجشنبه',
        'Fri':'جمعه',
        }
    

class Index:
    def __init__(self,name:str, value:str, time:str, date:str) -> None:
        self._name = name
        self._value = value
        self._time = time
        self._date = date
   
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
    @property
    def date(self):
        return self._date
   
    @date.setter
    def date(self,date):
        self._date = date

    @date.getter
    def date(self):
        return self._date

def code_to_name(code):
     
    return request_indx.setdefault(code) 
#make a dict with all wanted index that has default 0 value
def initTotalIndexs():
    total_indexs = dict()
    for id, name  in request_indx.items():
        total_indexs[id] = Index(name,'0','0','0')
    
    return total_indexs
 

class History:
    def __init__(self) -> None:
        self._data =list()
        self._max_value = 0
        self._min_value = 0 
        self._min_day_distance = 0
        self._max_day_distance = 0
        self._days= 0

    @property
    def data(self):
        return self._data
    @data.setter
    def data(self,data):
        self._data.append(data)
    @data.getter
    def data(self):
        return self._data

    @property
    def max_value(self):
        return self._max_value
    @max_value.setter
    def max_value(self,max_value):
        self._max_value = max_value
    @max_value.getter
    def max_value(self):
        return self._max_value

    @property
    def min_value(self):
        return self._min_value
    @min_value.setter
    def min_value(self,min_value):
        self._min_value = min_value
    @min_value.getter
    def min_value(self):
        return self._min_value
    
    @property
    def max_day_distance(self):
        return self._max_day_distance
    @max_day_distance.setter
    def max_day_distance(self,max_day_distance):
        self._max_day_distance = max_day_distance
    @max_day_distance.getter
    def max_day_distance(self):
        return self._max_day_distance

    @property
    def min_day_distance(self):
        return self._min_day_distance
    @min_day_distance.setter
    def min_day_distance(self,min_day_distance):
        self._min_day_distance = min_day_distance
    @min_day_distance.getter
    def min_day_distance(self):
        return self._min_day_distance
    @property
    def days(self):
        return self._days
    @days.setter
    def days(self,days):
        self._days = days
    @days.getter
    def days(self):
        return self._days

class DateTime:
    def __init__(self) -> None:
        
        self.date_time = jdatetime.datetime.now()
        self.date_time = self.date_time.astimezone(timezone('Asia/Tehran'))
        self.date = self.date_time.date()
        self.date_time = self.date_time.strftime('%a %d %m %Y %H %M %S') 
        self.weekday,self.day,self.month,self.year,self.hour,self.minute,self.second = self.date_time.split(' ')
        self.weekday = weekdays[self.weekday]
        self.month_str = months[self.month]  

