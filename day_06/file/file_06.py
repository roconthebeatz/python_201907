# -*- coding: utf-8 -*-

# CSV 포맷으로 저장된 데이터를 읽어오는 방법
# 1. 문자열 분할을 사용하여 처리하는 방법(기본 API)
input_file_name = "data/scores.txt"
input_file = open(input_file_name, "r")

scores = input_file.readlines()
print(scores)

for score in scores :
    data = score.strip().split(",")

    print(f"1번째 성적 : {int(data[0])} 점")
    print(f"2번째 성적 : {int(data[1])} 점")
    print(f"3번째 성적 : {int(data[2])} 점")
    
    print(f"총점 : {int(data[3])} 점, ", end='')
    print(f"평균 : {float(data[4]):.2f} 점")
    
    print("=" * 30)

input_file.close()


















