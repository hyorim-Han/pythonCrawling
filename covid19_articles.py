import csv

# 기사 개수를 세기 위한 변수 설정
cnt = 0

# 현재 폴더의 csv파일을 읽기 전용으로 열기
f = open('./covid19_articles.csv', 'r')

# 데이터를 딕셔너리 형태로 저장
lines = csv.DictReader(f)

# '뉴스기사제목' key의 value가 '[속보]'를 포함하면 출력 후 cnt++
for line in lines:
    if line['뉴스기사제목'].find('[속보]') != -1:
        print(line['뉴스기사제목'])
        cnt+=1

# 속보 기사 개수 출력
print('속보 기사 개수 : ', cnt)