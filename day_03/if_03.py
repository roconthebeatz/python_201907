# -*- coding: utf-8 -*-

# 기본 입력(키보드 입력)을 처리하는 방법
# - input 함수를 사용하여 키보드로부터 값을 입력받을 수 있음
# 사용법
# 변수명 = input()
#key_input = input()

# 변수명 = input(메세지)
key_input = input("정수를 입력하세요 : ")
print(f"key_input -> {key_input}")

# input 함수의 결과는 문자열 타입으로 반환됩니다.
# 만약 input 함수의 결과를 정수로 활용하려는 경우
# 형변환 과정을 거쳐야합니다.
# 문자열 -> 정수 : int함수
# 문자열 -> 실수 : float함수
# 문자열 -> 진리형 : bool함수
# 문자열이아닌값 -> 문자열 : str함수
#output = key_input + 2
#print(f"output -> {output}")

# 문자열로 정의된 "10" 이 정수 10으로 변경되어
# intValue 변수로 대입됨
# 문자열(str) -> 정수(int)
intValue = int("10")
print(type(intValue))

# 문자열로 정의된 "55.15" 가 실수 55.15로 변경되어
# floatValue 변수로 대입됨
# 문자열(str) -> 실수(float)
floatValue = float("55.15")
print(type(floatValue))

# 정수형 타입의 값인 intValue 변수의 값이
# 문자열로 변경되어 strValue로 대입
strValue = str(intValue)
print(type(strValue))

# 실수형 타입의 값인 floatValue 변수의 값이
# 문자열로 변경되어 strValue로 대입
strValue = str(floatValue)
print(type(strValue))

# 키보드로부터 입력된 정수가 문자열로 
# strNum변수에 대입
strNum = input("정수를 입력하세요 : ")
# strNum 변수의 값을 정수로 변환하여
# num 변수에 대입
num = int(strNum)

if num % 2 == 0 :
    print(f"입력된 값({num})은 짝수입니다.")

if num % 2 == 1 :
    print(f"입력된 값({num})은 홀수입니다.")









