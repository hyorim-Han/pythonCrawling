def get_papago_result(question):
    # 번역 입력 칸에 받아온 영단어 입력
    driver.find_element_by_css_selector('textarea#txtSource').send_keys(question)
    # 번역하기 버튼 클릭
    driver.find_element_by_css_selector('button#btnTranslate').click()
    time.sleep(1)
    # 번역한 결과 저장 및 출력
    output = driver.find_element_by_css_selector('div#txtTarget').text
    # 입력 칸 비우기
    driver.find_element_by_css_selector('textarea#txtSource').clear()
    return output

from selenium import webdriver
import time

my_dict = {}

# 크롬 창 열기
driver = webdriver.Chrome('./chromedriver')
papago_url = 'https://papago.naver.com/'
driver.get(papago_url)
time.sleep(3)

for _ in range(5):
    # 번역하고 싶은 영단어 입력받기
    question = input('번역할 영단어 입력 : ')
    # 번역된 단어 딕셔너리에 저장
    my_dict[question] = get_papago_result(question)

# 딕셔너리 출력
print(my_dict)

# 크롬 창 닫기
driver.close()
