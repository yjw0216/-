# pip install selenium

from selenium import webdriver as wd
import time

# 기본 접속 사이트
MAIN_URL = 'http://tour.interpark.com/'

# 브라우저 띄우기
driver = wd.Chrome( executable_path = './chromedriver.exe' )

# 접속
driver.get( MAIN_URL )

# 캡쳐(고스트에 주로함)
# driver.save_screenshot('main.png')

# 검색 (검색창의 html id : SearchGNBText << 검사로 알아냄 )
# 사이트페이지가 로드되는 것 (= 브라우저 메모리에 로드 되는 시점 )
driver.implicitly_wait(2)  ## 2초 기다렸다가 진행해라
driver.find_element_by_id('SearchGNBText').send_keys('파리')   ## find_id로 검색창 찾고 , send key로 검색어 넣고 

# 검색버튼 검사 >> search-btn란 class가 고유함을 알 수 있음 (ctrl + F 로 html 찾아보니까)
driver.find_element_by_class_name('search-btn').click()

driver.implicitly_wait(2)

driver.find_element_by_class_name('tour').click()

driver.implicitly_wait(2)

driver.find_element_by_id('SearchGNBText').send_keys('하와이') 

driver.find_element_by_class_name('search-btn').click()