def get_papago_result(keyword):
    # 번역 입력 칸에 받아온 영단어 입력
    driver.find_element_by_css_selector('textarea#txtSource').send_keys(keyword)
    # 번역하기 버튼 클릭
    driver.find_element_by_css_selector('button#btnTranslate').click()
    time.sleep(1)
    # 번역한 결과 저장
    output = driver.find_element_by_css_selector('div#txtTarget').text
    wtr.writerow([keyword, output])
    # 입력 칸 비우기
    driver.find_element_by_css_selector('textarea#txtSource').clear()
    

import csv
import time
from selenium import webdriver

driver = webdriver.Chrome()
papago_url = 'https://papago.naver.com/'
driver.get(papago_url)
time.sleep(3)

f = open('./papago.csv', 'w', newline = '')
wtr = csv.writer(f)

wtr.writerow(['영단어', '번역결과'])

while True:
    keyword = input('번역할 영단어 입력 (0을 입력하면 종료) : ')
    if keyword == '0':
        print('번역 종료')
        break
    
    get_papago_result(keyword)

driver.close()
f.close()