# -*- coding: utf-8 -*-

# 예외처리 문법
# try : 
#   예외가 발생할 가능성이 있는 코드
# except : 
#   예외가 발생한 경우 처리 코드
# else :
#   예외가 발생하지 않은 경우의 실행코드
# finally :
#   예외의 발생 여부와 상관없이 실행되는 코드

# 예외가 발생될 가능성이 있는 코드
#n1 = int(input("정수 입력 : "))
#n2 = int(input("정수 입력 : "))
#r = n1 / n2
#print(f"r -> {r}")

try :
    n1 = int(input("정수 입력 : "))
    n2 = int(input("정수 입력 : "))
    r = n1 / n2
except :
    print(f'예외 발생! 입력된 값({n1}, {n2})')
else :
    print(f'{n1} / {n2} = {r}')
finally :
    print('프로그램 종료')

















