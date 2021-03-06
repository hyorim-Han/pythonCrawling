import requests
from bs4 import BeautifulSoup

keyword = input('뉴스 검색 키워드 : ')
count = 0

hankyung_url1 = 'https://search.hankyung.com/apps.frm/search.news?query=' + keyword + '&page=1'
raw = requests.get(hankyung_url1)

soup = BeautifulSoup(raw.text, 'html.parser')
box = soup.find('div', {'class':'secion_cont'})
title = box.find_all('em', {'class':'tit'})
date_time = box.find_all('span', {'class':'date_time'})

while(title):
    print('['+date_time[count]+']  '+ title[count])
    count=+1

hankyung_url2 = 'https://search.hankyung.com/apps.frm/search.news?query=' + keyword + '&page=2'

