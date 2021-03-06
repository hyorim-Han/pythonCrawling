def get_papago_result(keyword):
    # 번역 입력 칸에 받아온 영단어 입력
    driver.find_element_by_css_selector('textarea#txtSource').send_keys(keyword)
    # 번역하기 버튼 클릭
    driver.find_element_by_css_selector('button#btnTranslate').click()
    time.sleep(1)
    # 번역한 결과 저장 및 출력
    output = driver.find_element_by_css_selector('div#txtTarget').text
    print(keyword, ' : ', output)
    # 입력 칸 비우기
    driver.find_element_by_css_selector('textarea#txtSource').clear()

import csv
import time
from selenium import webdriver

# 크롬 창 열기
driver = webdriver.Chrome()
papago_url = 'https://papago.naver.com/?sk=ko&tk=en'
driver.get(papago_url)
time.sleep(3)

# csv파일 내용 받아오기
f = open('./papago.csv', 'r')
rdr = csv.reader(f)
next(rdr)

# 한국어 번역 결과만 저장 후 파일 닫기
keywords = []
for row in rdr:
    keywords.append(row[1])
f.close()

# 번역 결과 출력
for keyword in keywords:
    get_papago_result(keyword)

# 파일 닫기
driver.close()