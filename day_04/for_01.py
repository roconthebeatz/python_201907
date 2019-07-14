# -*- coding: utf-8 -*-

# 반복문 - for 문
# while 반복문의 경우 조건식을 기준으로 반복의 여부를 결정
# (불특정한 횟수의 반복을 제어하는 경우에 사용)
# 반면, 특정 리스트, 딕셔너리, Set 내부의 데이터를 순회하는 경우
# whilt 반복문을 데이터의 추출을 위한 부가적인 작업들을 진행

numbers = [1,2,3,4,5,6,7,8,9,10]

# while 문을 사용한 리스트 내부의 데이터 순회

# 리스트 내부의 위치(인덱스)를 지정하는 변수
index = 0
size = len(numbers)

while index < size :
    value = numbers[index]
    print(f"numbers[{index}] -> {value:2}")
    
    # index의 값을 조정하여 반복문이 종료될 수 있도록 제어
    index += 1
    
print("프로그램 종료 - while")

# for 문을 사용하여 numbers 리스트의 데이터를 순회하는 과정
for value in numbers :
    print(f"value -> {value:2}")

print("프로그램 종료 - for")















