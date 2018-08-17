from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.request import urlopen
import time
import pandas as pd
from selenium.webdriver.common.keys import Keys
   
MAIN_URL = 'https://www.instagram.com/accounts/login/'
driver = webdriver.Chrome(executable_path='C:/Users/USER/Python37/py_project/py_basic/py_test/chromedriver')
driver.implicitly_wait(10) # 특정요소가 나타날떄까지 기다려준다. 동적으로 움직이는걸 
                        # 기다려주는게 매우중요하다.
                        #hyeonwu@gmail.com
                        #meaningless15
driver.get(MAIN_URL)
#driver.find_element_by_xpath("""//*[@class=""]/span/section/main/article/div[2]/div[2]/p/a""").click()
driver.find_element_by_xpath("""//*[@class="js not-logged-in client-root"]/body/span/section/main/div/article/div/div[1]/div/form/div[1]/div/div/input""").send_keys('ysw01044@naver.com ')
time.sleep(2)
driver.find_element_by_xpath("""//*[@class="js not-logged-in client-root"]/body/span/section/main/div/article/div/div[1]/div/form/div[2]/div/div/input""").send_keys('@wldnjs0216')
time.sleep(2)
driver.find_element_by_xpath("""//*[@class="js not-logged-in client-root"]/body/span/section/main/div/article/div/div[1]/div/form/span[1]/button""").click()
driver.find_element_by_xpath("""//*[@placeholder="검색"]""").send_keys("kimmira___")
driver.find_element_by_xpath("""//*[@class="js logged-in client-root"]/body/span/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a""").click()                                      
followerNum = driver.find_element_by_xpath("""//*[@class="js logged-in client-root"]/body/span/section/main/div/header/section/ul/li[2]/a/span""")
print(followerNum.text)
followerNum2 = followerNum.text.replace(',','') 

driver.find_element_by_xpath("""//*[@class="js logged-in client-root"]/body/span/section/main/div/header/section/ul/li[2]/a""").click()
time.sleep(2)

                                                                   
body = driver.find_element_by_tag_name('body')

for i in range(int(int(followerNum2)/5)):
    body.click()
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2)
    
tmpList = []
j=0                             
for i in range(1,int(followerNum2)+1):                                       
    c = driver.find_element_by_xpath("""//*[@class="js logged-in client-root"]/body/div[3]/div/div[2]/div/div[2]/ul/div/li[%s]/div/div[1]/div/div[1]/a"""%i)
    d = driver.find_element_by_xpath("""//*[@class="js logged-in client-root"]/body/div[3]/div/div[2]/div/div[2]/ul/div/li[%s]/div/div[1]/div/div[2]"""%i)
    tmp = d.text
    if not d.text :
        tmp ="null" 
    print(c.text)
    print(tmp)
    tmpList.append(tmp)

print(tmpList)
    
                                