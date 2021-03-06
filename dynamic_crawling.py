############ 동적크롤링 ############

from selenium import webdriver
import time

# webdriver에 chromedriver.exe 객체 생성하여 driver에 저장
# 가상의 크롬 창을 열 수 있도록 도와주는 속성값과 행동들을 driver 변수에 저장
driver = webdriver.Chrome('./chromedriver')

# 내장함수 get
# 입력한 url로 접속
# driver.get(url)
papago_url = 'https://papago.naver.com/'
driver.get(papago_url)
time.sleep(3)
driver.close()

# find_element_by_css_selector
driver.find_element_by_css_selector('a#writeFormBtn')

# find_element_by_id & find_element_by_class_name
driver.find_element_by_id('writeFormBtn')
driver.find_element_by_class_name('btn_type1.post_write._rosRestrict')

# find_element_by_xpath(적당한 id 혹은 class등의 속성이 없을 경우)
# html 요소 우클릭 - copy - copy xpath
driver.find_element_by_xpath('XPath 선택자')

# find_elements_by_??()
# find_element_~와 기능은 동일하나, 태그와 선택자에 부합하는 모든 내용 찾음

# click()
# html 요소를 클릭해주는 함수
driver.find_element_by_class_name('a#writeFormBtn').click()

# send_keys()
# html 요소에 직접 텍스트를 입력하는 함수
driver.find_element_by_css_selector('input#query').send_keys('파이썬')

# 열린 탭 목록 출력
driver.window_handles

# 열린 탭 개수
len(driver.window_handles)

# 첫 번째 탭
driver.window_handles[0]

# n번쨰 탭
driver.window_handles[n-1]

# 마지막에 열린 탭
driver.window_handles[-1]

# 탭 전환
driver.switch_to.window(driver.window_handles[-1])
driver.close() # 현재 탭만 닫아줌
driver.switch_to.window(driver.window_handles[0])