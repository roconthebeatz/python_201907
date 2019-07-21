# -*- coding: utf-8 -*-

# 파일의 내용을 한줄이 아닌 경우의 처리 방법
# readlines 메소드와 반복문을 활용하여 
# 처리할 수 있습니다.
input_file_name = "data/file_02_gugudan.txt"
input_file = open(input_file_name, "r")

input_data = input_file.readlines()
print(type(input_data))

# 대용량의 데이터인 경우 일괄작업보다는 
# 개별작업이 작업 부하를 줄일 수 있습니다.
#input_data = list(map(lambda x:x.strip(), input_data))

for data in input_data :    
    # 개행문자가 포함된 문자열
    # print(data)
    # 개행문자를 제거한 후 출력
    # print(data.strip())
    # print 함수의 자동 개행을 제어하여 출력
    print(data, end='')

input_file.close()









