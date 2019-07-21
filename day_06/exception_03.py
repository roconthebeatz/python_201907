# -*- coding: utf-8 -*-

# 예외처리 시, except 절을 정의하게 되면
# 어떠한 예외가 발생하더라도
# 동일한 예외처리 코드를 실행합니다
# 만약, 지정한 예외만 처리하고자 하는 경우
# 예외 클래스를 정의하여 처리할 수 있습니다.
# - except 예외클래스 as 예외의 메세지를 전달받을 변수 :
# -     정의된 예외가 발생한 경우 처리할 코드 ...
try :
    n1 = int(input('정수 입력 : '))
    n2 = int(input('정수 입력 : '))
    r = n1 / n2
except ZeroDivisionError as msg :
    print(f'예외 발생! 입력된 값({n1}, {n2})')
    print(f'예외 메세지 : {msg}')
else :
    print(f'{n1} / {n2} = {r}')
finally :
    print('프로그램 종료')
