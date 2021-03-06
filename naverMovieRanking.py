def dateCheck(date):
    year = int(date / 10000)
    month = int((date % 10000)/100)
    day = int(date % 100)
    month_day = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    # 월 요류 체크
    if (month > 12) | (month < 1):
        return False
    # 일 오류 체크
    elif (day > month_day[month]) | (day < 1):
        # 윤년 + 2월 29일인 경우 참값 리턴
        if (month == 2) & (day == 29):
            if ((year % 4 == 0) & ((year % 100 != 0) | (year % 400 == 0))) :
                return True
        return False
    # 년 오류 체크
    elif (year > datetime.date.today().year) | (year < 2004):
        return False
    # 아직 오지 않은 날짜 체크
    elif ( year == datetime.date.today().year ) & ( (month > datetime.date.today().month) | (day > datetime.date.today().day) ):
        return False
    
    return True
          
import datetime
import requests
from bs4 import BeautifulSoup

cnt = 1

while True:
    date = int(input('날짜 : '))
    if dateCheck(date) == True:
        break
    print('유효한 날짜를 입력해주세요.')

rank_url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=cnt&tg=1&date=' + str(date)

raw = requests.get(rank_url)
soup = BeautifulSoup(raw.text, 'html.parser')

box = soup.find('tbody')
titles = box.find_all('a')

print('< ', date, ' 기준 영화 순위 >')
print('[ Drama Charts ]')
for title in titles:
    print(cnt, ' . ', title.text)
    cnt+=1

    