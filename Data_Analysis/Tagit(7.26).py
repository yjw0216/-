from selenium import webdriver
from urllib.request import urlopen
import time
import pandas as pd
from selenium.webdriver.common.keys import Keys
from pynput.mouse import Button,Controller

def getFollowerList(nickName):
    MAIN_URL = 'https://www.instagram.com/accounts/login/'
    driver = webdriver.Chrome(executable_path='C:/Users/USER/Python37/py_project/py_basic/py_test/chromedriver')
    driver.implicitly_wait(10) # 특정요소가 나타날떄까지 기다려준다. 동적으로 움직이는걸 
                            # 기다려주는게 매우중요하다.
                            #hyeonwu@gmail.com
                            #meaningless15
    driver.get(MAIN_URL)
    driver.find_element_by_xpath("""//*[@class="js not-logged-in client-root"]/body/span/section/main/div/article/div/div[1]/div/form/div[1]/div/div/input""").send_keys('ysw01044@naver.com ')
    time.sleep(2)
    driver.find_element_by_xpath("""//*[@class="js not-logged-in client-root"]/body/span/section/main/div/article/div/div[1]/div/form/div[2]/div/div/input""").send_keys('@wldnjs0216')
    time.sleep(2)
    driver.find_element_by_xpath("""//*[@class="js not-logged-in client-root"]/body/span/section/main/div/article/div/div[1]/div/form/span[1]/button""").click()
    driver.find_element_by_xpath("""//*[@placeholder="검색"]""").send_keys("%s"%nickName)
    driver.find_element_by_xpath("""//*[@class="js logged-in client-root"]/body/span/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a""").click()                                      
    tmp_followerNum = driver.find_element_by_xpath("""//*[@class="js logged-in client-root"]/body/span/section/main/div/header/section/ul/li[2]/a/span""")
    followerNum = int(tmp_followerNum.text.replace(',','')) 

    driver.find_element_by_xpath("""//*[@class="js logged-in client-root"]/body/span/section/main/div/header/section/ul/li[2]/a""").click()
    
    time.sleep(2)
                                                 
    body = driver.find_element_by_tag_name('body')

    for i in range(int(followerNum/5)):
        body.click()
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.2)
        
    followerList = []                            
    for i in range(1,followerNum+1):                                       
        c = driver.find_element_by_xpath("""//*[@class="js logged-in client-root"]/body/div[3]/div/div[2]/div/div[2]/ul/div/li[%s]/div/div[1]/div/div[1]/a"""%i)
        d = driver.find_element_by_xpath("""//*[@class="js logged-in client-root"]/body/div[3]/div/div[2]/div/div[2]/ul/div/li[%s]/div/div[1]/div/div[2]"""%i)
        tmp_follower = d.text
        if not d.text :
            tmp_follower ="null" 
        print(c.text)
        print(tmp_follower)
        followerList.append(tmp_follower)

    print(followerList)
def getFolloingList(nickName):
    MAIN_URL = 'https://www.instagram.com/accounts/login/'
    driver = webdriver.Chrome(executable_path='C:/Users/USER/Python37/py_project/py_basic/py_test/chromedriver')
    driver.implicitly_wait(10) # 특정요소가 나타날떄까지 기다려준다. 동적으로 움직이는걸 
                            # 기다려주는게 매우중요하다.
                            #hyeonwu@gmail.com
                            #meaningless15
    driver.get(MAIN_URL)
    driver.find_element_by_xpath("""//*[@class="js not-logged-in client-root"]/body/span/section/main/div/article/div/div[1]/div/form/div[1]/div/div/input""").send_keys('ysw01044@naver.com ')
    time.sleep(2)
    driver.find_element_by_xpath("""//*[@class="js not-logged-in client-root"]/body/span/section/main/div/article/div/div[1]/div/form/div[2]/div/div/input""").send_keys('@wldnjs0216')
    time.sleep(2)
    driver.find_element_by_xpath("""//*[@class="js not-logged-in client-root"]/body/span/section/main/div/article/div/div[1]/div/form/span[1]/button""").click()
    driver.find_element_by_xpath("""//*[@placeholder="검색"]""").send_keys("%s"%nickName)
    driver.find_element_by_xpath("""//*[@class="js logged-in client-root"]/body/span/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a""").click()                                      
    tmp_followerNum = driver.find_element_by_xpath("""//*[@class="js logged-in client-root"]/body/span/section/main/div/header/section/ul/li[3]/a/span""")
    followerNum = int(tmp_followerNum.text.replace(',','')) 

    driver.find_element_by_xpath("""//*[@class="js logged-in client-root"]/body/span/section/main/div/header/section/ul/li[3]/a""").click()
    time.sleep(2)                                             

    body = driver.find_element_by_tag_name('body')

    for i in range(int(followerNum/5)):
        body.click()
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.2)
        
    followerList = []                            
    for i in range(1,followerNum+1):                                       
        ID = driver.find_element_by_xpath("""//*[@class="js logged-in client-root"]/body/div[3]/div/div[2]/div/div[2]/ul/div/li[%s]/div/div[1]/div/div[1]/a"""%i)
        Name = driver.find_element_by_xpath("""//*[@class="js logged-in client-root"]/body/div[3]/div/div[2]/div/div[2]/ul/div/li[%s]/div/div[1]/div/div[2]"""%i)
        tmp_follower = Name.text
        if not Name.text :
            tmp_follower ="null" 
        print(ID.text)
        print(tmp_follower)
        followerList.append(tmp_follower)

    print(followerList)    
def getLikeList(nickName):
    MAIN_URL = 'https://www.instagram.com/accounts/login/'
    driver = webdriver.Chrome(executable_path='C:/Users/USER/Python37/py_project/py_basic/py_test/chromedriver')
    driver.implicitly_wait(10) # 특정요소가 나타날떄까지 기다려준다. 동적으로 움직이는걸 
                            # 기다려주는게 매우중요하다.
                            #hyeonwu@gmail.com
                            #meaningless15
    driver.get(MAIN_URL)
    driver.find_element_by_xpath("""//*[@class="js not-logged-in client-root"]/body/span/section/main/div/article/div/div[1]/div/form/div[1]/div/div/input""").send_keys('ysw01044@naver.com ')
    time.sleep(2)
    driver.find_element_by_xpath("""//*[@class="js not-logged-in client-root"]/body/span/section/main/div/article/div/div[1]/div/form/div[2]/div/div/input""").send_keys('@wldnjs0216')
    time.sleep(2)
    driver.find_element_by_xpath("""//*[@class="js not-logged-in client-root"]/body/span/section/main/div/article/div/div[1]/div/form/span[1]/button""").click()
    driver.find_element_by_xpath("""//*[@placeholder="검색"]""").send_keys("%s"%nickName)
    driver.find_element_by_xpath("""//*[@class="js logged-in client-root"]/body/span/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a""").click()
    tmp_contentNum = driver.find_element_by_xpath("""//*[@class="js logged-in client-root"]/body/span/section/main/div/header/section/ul/li[1]/span/span""")
    contentNum = int(tmp_contentNum.text.replace(',','')) 
    print('게시물 수 : ', contentNum)
                          
    driver.find_element_by_xpath("""//*[@id="react-root"]/section/main/div/div[2]/article/div/div/div[1]/div[1]/a/div[1]/div[2]""").click()

    time.sleep(2)
    j=0
    for i in range(contentNum):
        tmp =driver.find_element_by_xpath("""//*[@class="js logged-in client-root"]/body/div[3]/div/div[2]/div/article/div[2]/section[2]/div""").text
        print(tmp)
        if '조회' in tmp:
            print(' 성공이다')
            if j == 0 :
                if j == contentNum-1:
                    pass
                else:  
                    if j == contentNum-1:
                        pass
                    else:  
                        driver.find_element_by_xpath("""//*[@class="js logged-in client-root"]/body/div[3]/div/div[1]/div/div/a""").click()
                        print('click')
                        time.sleep(2)
            else:
                driver.find_element_by_xpath("""//*[@class="js logged-in client-root"]/body/div[3]/div/div[1]/div/div/a[2]""").click()
                print('click2')
                time.sleep(3)
        elif '좋아요' in tmp:
            time.sleep(1)
            tmp_Num1 =tmp.replace('좋아요','')
            tmp_Num2 =tmp_Num1.replace('개','')
            tmp_Num3 =int(tmp_Num2.replace(' ',''))
                                                                                                                    
            driver.find_element_by_xpath("""//*[@class="js logged-in client-root"]/body/div[3]/div/div[2]/div/article/div[2]/section[2]/div/a""").click()
            time.sleep(2)
            mouse = Controller()
            ###########################################
            
            mouse.position = (800, 500)
            print(tmp_Num3)
            print('now is {0}'.format(mouse.position))
            for i in range(int(tmp_Num3/3)):
                print(i)
                if i%2 == 0 :
                    mouse.move(10,-10)
                else:
                    mouse.move(-10,10)
                mouse.scroll(0,-1000)
                time.sleep(0.2)
            
        
            ###########################################
            likeList = []                            
            for i in range(1,tmp_Num3+1):                  
                                                                                                 
                ID = driver.find_element_by_xpath("""//*[@class="js logged-in client-root"]/body/div[3]/div/div[2]/div/article/div[2]/div[2]/ul/div/li[%s]/div/div[1]/div/div[1]/a"""%i)
                Name = driver.find_element_by_xpath("""//*[@class="js logged-in client-root"]/body/div[3]/div/div[2]/div/article/div[2]/div[2]/ul/div/li[%s]/div/div[1]/div/div[2]"""%i)
                tmp_like = Name.text
                if not Name.text :
                    tmp_like ="null" 
                print(ID.text)
                print(tmp_like)
                likeList.append(tmp_like)
            print(likeList)
            if j == 0:
                if j == contentNum-1:
                    pass
                else:
                    driver.find_element_by_xpath("""//*[@class="js logged-in client-root"]/body/div[3]/div/div[1]/div/div/a""").click()
                    time.sleep(2)            
            elif j == contentNum-1:
                pass
            else:
                driver.find_element_by_xpath("""//*[@class="js logged-in client-root"]/body/div[3]/div/div[1]/div/div/a[2]""").click()    
                time.sleep(2)
        else:
            if j == 0:
                if j == contentNum-1:
                    pass
                else:    
                    driver.find_element_by_xpath("""//*[@class="js logged-in client-root"]/body/div[3]/div/div[1]/div/div/a""").click()
                    time.sleep(2)            
           
            else:
                if j == contentNum-1:
                    pass
                else:
                    driver.find_element_by_xpath("""//*[@class="js logged-in client-root"]/body/div[3]/div/div[1]/div/div/a[2]""").click()    
                    time.sleep(2)
            pass
        j = j + 1
            
    

# 문제 봉착 : 동영상게시물은 좋아요리스트가아닌 조회숫자가 나온다.

    
    
                  

if __name__ == '__main__':
    tmp = input('닉네임 : ')
    getLikeList(tmp)
                                