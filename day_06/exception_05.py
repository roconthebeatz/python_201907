# -*- coding: utf-8 -*-

# 어떠한 예외가 발생하더라도 처리할 수 있는 예외 클래스
# - 모든 예외클래스의 최상위 부모 클래스를 사용하여 처리
# - Exception 클래스
# - Exception 클래스의 타입은 어떠한 예외 타입이 전달되어도
#   값을 받을 수 있는 타입으로 모든 예외를 처리할 수 있습니다.

# Exception 클래스를 사용한 예외처리 방법
# - except 예외클래스1  :
# -     예외클래스1 타입이 발생한 경우 처리할 코드 ...
# - except 예외클래스2  :
# -     예외클래스2 타입이 발생한 경우 처리할 코드 ...
# - except Exception  :
# -     예외클래스1, 예외클래스2 타입이 아닌 어떠한 
#       예외가 발생하더라도 처리할 수 있는 영역
try :
    n1 = int(input('정수 입력 : '))
    n2 = int(input('정수 입력 : '))
    r = n1 / n2
except ZeroDivisionError as msg :
    # / 0 연산이 실행되는 경우
    print(f'ZeroDivisionError 예외 발생!')
    print(f'예외 메세지 : {msg}')
except Exception :
    # ZeroDivisionError 가 아닌 예외 발생 시 실행되는 영역
    print(f'Exception 예외 발생!')    
else :
    print(f'{n1} / {n2} = {r}')
finally :
    print('프로그램 종료')







