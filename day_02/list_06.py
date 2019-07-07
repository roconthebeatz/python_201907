# -*- coding: utf-8 -*-

# 리스트 타입의 데이터 결합
# - 리스트 타입의 변수들은 결합될 수 있습니다.
list_front = [1, 2, 3, 4, 5]
list_end = [6, 7, 8, 9]

# + 연산을 통해서 결합을 처리할 수 있음
list_merge = list_front + list_end
print(f"merge : {list_merge}")

# + 연산을 통한 리스트의 결합 시, 완전 복제로 구현됩니다.
# - list_merge의 각 구성요소의 값을 수정해도
#   원본데이터 list_front, list_end의 값은 수정되지 않음
list_merge[0] = 1000

print(f"front : {list_front}")
print(f"end : {list_end}")
print(f"merge : {list_merge}")

# 리스트의 반복 연산
# * 연산자를 사용하여 리스트의 내용을
# 반복한 결과를 저장할 수 있습니다.
numbers = [1,2,3]
numbers_multiply = numbers * 3

print(f"numbers -> {numbers}")
print(f"multiply -> {numbers_multiply}")




















