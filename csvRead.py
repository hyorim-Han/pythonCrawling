import csv

# 현재 폴더에 있는 csv파일을 읽기 전용으로 열기
f = open('./example.csv', 'r')

# csv 파일의 모든 데이터를 저장
rdr = csv.reader(f)

# 첫 번째 행은 건너뛰고 출력하고 싶을 때
next(rdr)

# 저장된 데이터 행별로 출력
for row in rdr:
    print(row)

# 파일 닫기
f.close()
