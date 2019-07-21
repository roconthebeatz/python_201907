# -*- coding: utf-8 -*-

numbers = [10, 17, 9, 5, 37]

# 리스트를 순회하는 for 문
# 리스트 내부의 값을 순차적으로 추출하여
# 반복을 수행 (인덱스 정보 X)
for data in numbers : 
    print(f"data -> {data}")

print("*" * 15)

# for 문에서 인덱스 정보를 활용하기 위한 코드
# 직접 변수를 생성하여 제어하는 방식
index = 0
for data in numbers : 
    print(f"numbers[{index}] -> {data}")
    index += 1

print("*" * 15)

# enumerate 함수
# 매개변수 전달된 컬렉션 내부의 데이터를 인덱스 정보를 포함하여
# 하나씩 추출하는 함수입니다.
for index, data in enumerate(numbers) : 
    print(f"numbers[{index}] -> {data}")









