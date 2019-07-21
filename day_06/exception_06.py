# -*- coding: utf-8 -*-

# 2개의 정수를 입력받아 리스트에 추가한 후,
# 두 정수의 나눈 결과를 리스트에 추가하여
# 리스트 내부의 데이터를 출력하세요.

# 2개의 정수 및 나눈 결과를 저장하기 위한
# 리스트 변수의 선언
numbers = []

# 무한루프를 구현하는 반복문
# - 종료되지 않는 반복문
# - 반복문의 내부에서 반복문을 종료하기 위한
#   break 키워드를 정의해야함
while True :
    # 입력 과정을 처리
    numbers.append(int(input('정수1 입력 : ')))
    numbers.append(int(input('정수2 입력 : ')))
    
    try :
        result = numbers[0] / numbers[1]
    except :
        # 만약 / 연산에서 예외가 발생하는 경우
        # 다시 정수를 입력받기 위해서
        # 리스트 내부의 데이터를 제거
        numbers.clear()
        print(" / 0은 허용되지 않습니다.")
    else : 
        # / 결과에 문제가 없다면
        # 반복문을 종료함
        numbers.append(result)
        break
    finally :
        pass

print(f'numbers ->{numbers}')












