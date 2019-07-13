# -*- coding: utf-8 -*-

# 중첩된 반복문을 활용한 구구단 출력 예제

# 아래의 코드를 사용하여 짝수 단을 출력하는
# 코드를 완성하세요.

dan = 2

while dan < 10 :
    if dan % 2 == 0 :
        print(f"{dan}단을 출력합니다.")
        
        mul = 1
        while mul < 10 :
            print(f"{dan} * {mul} = {dan * mul}")
            mul += 1
        
        print()
    dan += 1
    
print("프로그램 종료")












