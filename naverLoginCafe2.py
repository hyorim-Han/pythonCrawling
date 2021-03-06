# 글 내용 출력하는 함수
def print_content():
    driver.find_element_by_css_selector('a.BaseButton.btn_next.BaseButton--skinGray.size_default').click()
    time.sleep(3)
    content = driver.find_element_by_css_selector('div.se-module.se-module-text').text
    print('< ', cnt, '번째 글 >')
    print(content,'\n')

    return cnt+1

from selenium import webdriver
import time

cnt = 1

# 크롬 창 열기
driver = webdriver.Chrome()
login_url = 'https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com'
driver.get(login_url)
time.sleep(2)

# 로그인
my_id = 'ekqls0458'
my_pw = '981hyo125^^'

driver.execute_script("document.getElementsByName('id')[0].value = \'" + my_id + "\'")
driver.execute_script("document.getElementsByName('pw')[0].value = \'" + my_pw + "\'")
time.sleep(1)

driver.find_element_by_id('log.login').click()
time.sleep(1)
driver.find_element_by_id('new.save').click()

# 카페 접속
comu_url = 'https://cafe.naver.com/codeuniv'
driver.get(comu_url)
time.sleep(1)

# 신규회원게시판 접속
driver.find_element_by_id('menuLink90').click()
time.sleep(1)

# 프레임 전환
driver.switch_to.frame('cafe_main')
time.sleep(3)

# 첫번째 글 클릭
driver.find_element_by_xpath('//*[@id="main-area"]/div[4]/table/tbody/tr[1]/td[1]/div[2]/div/a').click()
time.sleep(2)

# 글 내용 출력
cnt = print_content()

# 2~20번째 게시물 출력
for _ in range(19):
    cnt = print_content()

# 크롬 창 닫기
driver.close()