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
        'Far':'فروردین',
        'Ord':'اردیبهشت',
        'Kho':'خرداد',
        'Tir':'تیر',
        'Mor':'مرداد',
        'Sha':'شهریور',
        'Meh':'مهر',
        'Aba':'آبان',
        'Aza':'آذر',
        'Dey':'دی',
        'Bah':'بهمن',
        'Esf':'اسفند',
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
     
    return request_indx.setdefault(code) 
#make a dict with all wanted index that has default 0 value
def initTotalIndexs():
    total_indexs = dict()
    for id, name  in request_indx.items():
        total_indexs[id] = Index(name,'0','0')
    
    return total_indexs
 



class DateTime:
    def __init__(self) -> None:
        
        self.date_time = jdatetime.datetime.now()
        self.date_time = self.date_time.astimezone(timezone('Asia/Tehran'))
        self.date_time = self.date_time.strftime('%a %d %b %Y %H %M') 
        self.weekday,self.day,self.month,self.year,self.hour,self.minute = self.date_time.split(' ')
        self.weekday = weekdays[self.weekday]
        self.month_str = months[self.month]  