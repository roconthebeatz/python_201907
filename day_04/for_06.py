# -*- coding: utf-8 -*-

# 아래의 구구단 출력코드를 수정하여
# 홀수단의 구구단을 출력하세요.

for dan in range(2, 10) :
    
    if dan % 2 == 0 :
        continue
    
    print(f"{dan}단을 출력합니다.")
    
    for mul in range(1, 10) : 
        
        print(f"{dan} * {mul} = {dan * mul}")
        

