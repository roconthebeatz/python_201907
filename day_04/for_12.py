# -*- coding: utf-8 -*-

numbers = [11, 22, 33, 44, 55]

# numbers 리스트의 요소 중 홀수인 요소에는 10을 곱하고,
# 짝수인 경우에는 원본 데이터 그대로 유지하여
# numbers_copy 리스트를 생성하세요.

# 일반적인 반복 코드를 사용하여 처리하는 예제
#numbers_copy = []
#for data in numbers :
#    if data % 2 == 0 :
#        numbers_copy.append(data)
#    else:
#        numbers_copy.append(data*10)

# 리스트 변수의 생성에 for 반복문을 사용하는 방법
# (특정 조건에 만족하는 경우와 만족하지 않는 경우를 처리)
# 리스트변수명 = 
# [실행문1 if 실행문1의조건식 
#  else 실행문2(조건식이 거짓일 경우 실행되는 문장) 
#  for 변수명 in 컬렉션]
numbers_copy = \
[data * 10 if data % 2 == 1 else data for data in numbers]

print(numbers)
print(numbers_copy)











