from selenium import webdriver
import time

my_dict = {}

# 웹페이지 접속
driver = webdriver.Chrome('./chromedriver')
papago_url = 'https://papago.naver.com/'
driver.get(papago_url)
time.sleep(3)

# 검색할 영단어 받아오기
question = input('번역할 영단어 입력 : ')

# 번역 입력 칸에 받아온 영단어 입력
driver.find_element_by_css_selector('textarea#txtSource').send_keys(question)

# 번역하기 버튼 클릭
driver.find_element_by_css_selector('button#btnTranslate').click()
time.sleep(1)

# 번역한 결과 저장 및 출력
output = driver.find_element_by_css_selector('div#txtTarget').text

my_dict[question] = output
print(my_dict)

# 입력 칸 초기화
driver.find_element_by_css_selector('textarea#txtSource').clear()

# 크롬 창 닫기
driver.close()
