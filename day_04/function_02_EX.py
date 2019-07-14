# -*- coding: utf-8 -*-

# 구구단 전체를 출력할 수 있는 
# gugudan_all 함수를 선언하고 
# 호출 결과를 확인하세요

def gugudan_all() :
    for dan in range(2,10) :
        print(f"{dan}단을 출력합니다.")
        
        for mul in range(1,10) :
            
            print(f"{dan} * {mul} = {dan*mul}")
            
gugudan_all()

# 매개변수로 전달된 숫자에 해당되는
# 구구단을 출력할 수 있도록
# gugudan_one 함수를 선언하고
# 호출 결과를 확인하세요.
def gugudan_one(dan) :
    print(f"{dan}단을 출력합니다.")
    for mul in range(1, 10) :
        print(f"{dan} * {mul} = {dan*mul}")

gugudan_one(7)













