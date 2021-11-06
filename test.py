from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
import time


#html = urlopen('http://pythonscraping.com/pages/javascript/ajaxDemo.html')
#bs = BeautifulSoup(html, 'html.parser')
#print(bs.body.div.get_text())
driver = webdriver.Chrome('D:\\programming\\python\\begin\\')

driver.get('http://pythonscraping.com/pages/javascript/ajaxDemo.html')
time.sleep(3)
print(driver.find_element_by_id('content').text)
driver.close()