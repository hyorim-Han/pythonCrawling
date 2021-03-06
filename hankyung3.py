from selenium import webdriver
import time

# 키워드 입력
keyword = input('뉴스 검색 키워드 : ')

# 기사 개수를 세기 위한 변수
cnt = 0

# 한국경제뉴스페이지 접속
driver = webdriver.Chrome()
news_url = 'https://search.hankyung.com/apps.frm/search.news?query=' + keyword + '&mediaid_clust=HKPAPER,HKCOM'
driver.get(news_url)
time.sleep(2)

# 1페이지부터 3페이지까지 크롤링
for _ in range(2):
    # 현재 페이지의 뉴스 기사 제목 태그 저장
    ten_articles = driver.find_elements_by_css_selector('em.tit')

    # 기사 제목 title 변수에 저장 후 기사 클릭
    for article in ten_articles:
        title = article.text
        article.click()
        time.sleep(1)

        # 창 전환 후 기사 본문 \n으로 구분하여 content 변수에 저장
        driver.switch_to.window(driver.window_handles[-1])
        contents = driver.find_element_by_id('articletxt').text
        content = contents.split('\n')

        # 기사 출력(필요없는 공백 제거)
        cnt += 1
        print('< ',cnt, '번 뉴스 - ', title, '>')
        for con in content:
            if con != '':
                print(con, end = ' ')
        print('\n')

        # 기사 창 닫기
        driver.close()

        # 창 한국경제뉴스페이지로 전환
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(2)
    
    driver.find_element_by_class_name('next').click()


# 크롬 창 닫기
driver.close()