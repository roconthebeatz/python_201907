# -*- coding: utf-8 -*-

# csv 모듈
# csv 포맷으로 데이터를 저장하거나
# 불러오고자 하는 경우 손쉽게 사용할 수 있는
# 기능을 제공하는 모듈
import csv

# 성적점수를 입력받아 입력된 성적을 CSV 포맷으로 저장하는
# 프로그램을 작성

# 과목수
count = 3
# 성적 저장 변수
scores = []

for index in range(1, count+1) :
    temp = int(input(f"{index}번째 성적 입력 : "))
    scores.append(temp)

# print(scores)

# 정수 타입의 값은 join 될 수 없으므로
# 형변환 과정이 필요함
# save_csv = ",".join(scores)
# save_csv = ",".join(map(lambda x:str(x),scores))

# print(save_csv)

output_file_name = "data/file_08.txt"
# newline 옵션
# 개행 문자를 처리하기 위한 옵션 값
# 개행 문자를 newline 매개변수에 전달된 값으로
# 대체해서 출력할 수 있는 옵션
# w, a 모드에 사용
with open(output_file_name, "w", newline="") as output_file :
    # 파일에 CSV 포맷으로 출력할 수 있는
    # csv 모듈의 writer 객체 생성
    writer = csv.writer(output_file)
    writer.writerow(scores)
    
#    output_file.write(save_csv)













