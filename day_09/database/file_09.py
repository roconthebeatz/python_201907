# -*- coding: utf-8 -*-

import csv

input_file_name = "data/file_08.txt"

with open(input_file_name, "r") as input_file :
    # 파일을 읽을 수 있는 객체를 사용하여
    # CSV 모듈의 reader 객체를 생성하는 코드    
    reader = csv.reader(input_file)
    
    # CSV 모듈의 reader 객체는 for 문의 변수로
    # 활용되며 파일로부터 데이터를 한줄씩 추출할 수
    # 있습니다.
    # 추가적으로 추출된 데이터는 , 를 기준으로 
    # 자동으로 분류되어 리스트로 반환됩니다.
    for line in reader :
        print(line)
        print(f"첫번째 성적 : {line[0]}")
        print(f"두번째 성적 : {line[1]}")
        print(f"세번째 성적 : {line[2]}")
        
        
        
        
        
        
        