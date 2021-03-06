########### 정적크롤링 ############

# 라이브러리 불러오기(requests for html)
import requests 

lotto_url = 'https://dhlottery.co.kr/gameResult.do?method=byWin'

# 웹페이지 html코드 전체 받아오기
# value = requests.get(url)
raw = requests.get(lotto_url)

# <response [200]> 나오면 오케이
print(raw)

# raw변수의 값을 text형식으로 출력(문자열, 선택자 구분 X)
print(raw.text)

# 라이브러리 불러오기(beautifulsoup4 for html searching)
from bs4 import BeautifulSoup

# html 문자열 코드 선택자와 태그 구분
# Beautifulsoup(문자열, 'html.parser')
soup = BeautifulSoup(raw.text, 'html.parser')
print(soup)

print(type(raw.text)) #str
print(type(soup)) #bs4.BeautifulSoup

# 내장함수 find
# 찾는 정보 하나만 가져오고 싶을 때
# (html코드).find('div')
# (html코드).find(id = 'example1')
# (html코드).find(attrs = {'id':'example1'})
# (html코드).find('div', {'id':'example1'})
# 당첨 번호를 모두 포함하는 가장 작은 크기의 태그만 가져오기
box = soup.find('div', {'class':'nums'})

# 내장함수 find_all
# 해당 태그의 모든 html 코드 전체를 리스트 형태로 변환
# (html코드).find_all('div')
# (html코드).find_all(id = 'example')
# (html코드).find_all(['div','span'])
# (html코드).find_all(attrs = {'id':'example1','class':'example2'})
# 가져온 태그에서 당첨 번호만 추출
numbers = box.find_all('span')
print('<최근 로또 당첨 번호>')
for number in numbers:
    print(number.text)