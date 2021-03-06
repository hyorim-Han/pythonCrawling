import csv

# 현재 폴더에 있는 csv 파일을 추가 모드로 열기
f = open('./example.csv', 'a', newline = '')

# 작성을 위한 객체 변수 생성
wtr = csv.writer(f)

# 추가하고 싶은 행 작성
wtr.writerow(['바둑', 40, '파이썬'])

list = [['오목', 50, 'C'], ['장기', 60, '자바']]
wtr.writerows(list)

# 파일 닫기
f.close()