# -*- coding: utf-8 -*-

# map 함수
# filter 함수와 유사함.
# filter 함수의 경우 True, False 의 값을 반환하는
# 함수를 사용하여 특정 데이터를 필터링하는 역할을
# 하지만 map 함수는 특정 연산을 모든 요소에
# 적용하기 위해서 활용합니다.

# 함수의 실행 결과 
# filter 함수는 원본 데이터의 개수보다 작을 수 있음
# map 함수는 원본 데이터와 개수가 같음

numbers = [12,23,52,77,93]

# numbers 리스트의 모든 요소를 제곱한 새로운 리스트를
# 생성하는 예제

# 매개변수로 전달된 값을 제곱하여 반환하는 함수
def custom_pow(data) :
    return data * data

numbers_pow = list(map(custom_pow,numbers))
print(numbers_pow)

numbers_pow = list(map(lambda x : x * x, numbers))
print(numbers_pow)

# numbers 리스트 내부의 데이터 중, 짝수인 경우만
# 제곱하여 새로운 리스트를 생성하세요.
numbers_pow = list(map(lambda x:x*x, 
                        list(filter(lambda x:x%2==0, numbers))))
print(numbers_pow)























