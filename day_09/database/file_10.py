# -*- coding: utf-8 -*-

import csv

input_file_name = "data/file_10.txt"

with open(input_file_name, "r") as input_file :
    reader = csv.reader(input_file)
    
    for info in reader :
        print(f"계좌소유주 : {info[0]}, ", end="")
        print(f"잔액 : {info[1]}, ", end="")
        
        # 모든 계좌에 대해서 10% 증가된 값을 출력하세요.
        # $ 문자로 인해서 숫자 변경이 안됨
        #balance = float(info[1])
        balance = float(info[1].lstrip("$").replace(",",""))
        balance *= 1.1
        print(f"증가된 잔액 : {balance:.2f}")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        