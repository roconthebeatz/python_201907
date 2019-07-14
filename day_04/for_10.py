# -*- coding: utf-8 -*-

numbers = [10, 20, 30]

# numbers 리스트의 각 요소에 10을 곱하여
# numbers_copy 리스트를 생성하세요

# numbers 리스트의 모든 요소를 복사한
# 새로운 리스트를 생성하여 numbers_copy로 대입
#numbers_copy = numbers[:]
#print(numbers_copy)

# 비어있는 리스트 변수를 생성
#numbers_copy = []
#for data in numbers :
#    numbers_copy.append(data * 10)
#print(numbers_copy)

# 리스트 변수의 선언에 for문이 활용되는 예제
# 리스트변수명 = [실행문 for 변수명 in 컬렉션]
numbers_copy = [data*10 for data in numbers]

print(numbers)
print(numbers_copy)













