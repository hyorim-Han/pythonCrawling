def get_papago_result(keyword):
    # 번역 입력 칸에 받아온 영단어 입력
    driver.find_element_by_css_selector('textarea#txtSource').send_keys(keyword)
    # 번역하기 버튼 클릭
    driver.find_element_by_css_selector('button#btnTranslate').click()
    time.sleep(1)
    # 번역한 결과 저장
    output = driver.find_element_by_css_selector('div#txtTarget').text
    # 입력 칸 비우기
    driver.find_element_by_css_selector('textarea#txtSource').clear()
    
    return output


import csv
import time
from selenium import webdriver

driver = webdriver.Chrome()
papago_url = 'https://papago.naver.com/'
driver.get(papago_url)
time.sleep(3)

f = open('./papago.csv', 'r')

rdr = csv.reader(f)
next(rdr)

my_dict = {}
for row in rdr:
    keyword = row[0]
    korean = row[1]
    my_dict[keyword] = korean

f.close()

f = open('./papago.csv', 'a', newline = '')
wtr = csv.writer(f)

while True:
    keyword = input('번역할 영단어 입력 (0을 입력하면 종료) : ')
    if keyword == '0':
        print('번역 종료')
        break
    
    if keyword in my_dict.keys():
        print('이미 번역된 영단어입니다. 뜻은', my_dict[keyword], '입니다.')

    else:
        output = get_papago_result(keyword)
        wtr.writerow([keyword, output])
        my_dict[keyword] = output

driver.close()
f.close()