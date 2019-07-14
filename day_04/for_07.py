# -*- coding: utf-8 -*-

# 다음과 같이 구구단을 출력하세요
"""
2 * 2 = 4
2 * 4 = 8
2 * 6 = 12
...
3 * 1 = 3
3 * 3 = 9
3 * 5 = 15
...
4 * 2 = 8
4 * 4 = 16
4 * 6 = 24
...
"""
for dan in range(2, 10) :
    
    print(f"{dan}단을 출력합니다.")
    
    for mul in range(1, 10) : 
        
        if dan % 2 == mul % 2 :
            print(f"{dan} * {mul} = {dan * mul}")
        
        # 각 조건식의 결과를 변수로 저장한 후
        # if 문을 통해서 처리하는 방법
        # (일반적으로 변수를 사용하는 방법이
        # 가장 가독성이 높음)
#        flag_1 = (dan % 2 == 0 and mul % 2 == 0)
#        flag_2 = (dan % 2 == 1 and mul % 2 == 1)
#        if flag_1 or flag_2 :
#            print(f"{dan} * {mul} = {dan * mul}")
        
        # 단수와 곱해지는 수의 짝수/홀수 여부를
        # 비교하여 처리하는 방법
        # - 조건식의 길이 길어질수록 가독성이 떨어짐
#        if (dan % 2 == 0 and mul % 2 == 0) \
#        or (dan % 2 == 1 and mul % 2 == 1) :
#            print(f"{dan} * {mul} = {dan * mul}")
















