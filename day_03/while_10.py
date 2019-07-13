# -*- coding: utf-8 -*-

# 중첩된 반복문을 활용한 구구단 출력 예제

dan = 2

while dan < 10 :
    print(f"{dan}단을 출력합니다.")
    
    mul = 1
    while mul < 10 :
        print(f"{dan} * {mul} = {dan * mul}")
        mul += 1
    
    dan += 1
    print()
    
print("프로그램 종료")












