import csv

# 현재 폴더에 csv파일 쓰기전용으로 생성, 줄바꿈 해제
f = open('./example.csv','w', newline = '')

# 작성을 위한 객체 변수 생성
wtr = csv.writer(f)

# 열 제목
wtr.writerow(['이름', '나이', '언어'])

# 데이터 생성
all_name = ['길동', '철수', '영희']
all_age = [10, 20, 30]
all_language = ['파이썬', 'C', '자바']

# 데이터 작성(행별로)
for i in range(3):
    name = all_name[i]
    age = all_age[i]
    language = all_language[i]
    wtr.writerow([name, age, language])

# 파일 닫기 ★★★★★
f.close()