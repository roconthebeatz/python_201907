# -*- coding: utf-8 -*-

numbers = [11, 22, 33, 44, 55]

# numbers 리스트의 요소중 홀수인 요소에
# 10을 곱하여 numbers_copy 리스트를 생성하세요.

# 일반적인 처리 방식
#numbers_copy = []
#for data in numbers :
#    if data % 2 == 1 :
#        numbers_copy.append(data*10)

# 리스트 변수의 선언에 for문이 활용되는 예제
# (특정 조건에 만족하는 경우만 실행되도록 제어)
# 리스트변수명 = [실행문 for 변수명 in 컬렉션 if 조건식]
numbers_copy = \
[data*10 for data in numbers if data % 2 == 1]
        
print(numbers)
print(numbers_copy)










