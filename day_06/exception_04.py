# -*- coding: utf-8 -*-

# 다수개의 지정된 예외만 처리하기 위한 작성 방법
# - except 예외클래스1  :
# -     예외클래스1 타입이 발생한 경우 처리할 코드 ...
# - except 예외클래스2  :
# -     예외클래스2 타입이 발생한 경우 처리할 코드 ...
# - except 예외클래스N  :
# -     예외클래스N 타입이 발생한 경우 처리할 코드 ...
try :
    n1 = int(input('정수 입력 : '))
    n2 = int(input('정수 입력 : '))
    r = n1 / n2
except ZeroDivisionError as msg :
    # / 0 연산이 실행되는 경우
    print(f'ZeroDivisionError 예외 발생!')
    print(f'예외 메세지 : {msg}')
except ValueError :
    # 잘못된 입력이 실행되는 경우
    print(f'ValueError 예외 발생!')    
else :
    print(f'{n1} / {n2} = {r}')
finally :
    print('프로그램 종료')







