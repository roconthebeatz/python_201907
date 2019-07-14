# -*- coding: utf-8 -*-

# LIST 변수를 사용하여 사용자에게 3개의 정수를 입력받고
# 입력된 정수의 합계, 평균, 최대값, 최소값
"""
1번째 정수 : 10
2번째 정수 : 5
3번째 정수 : 20
입력된 정수 리스트 : [10, 5, 20]
합계 : 35, 평균 : 11.66, 최대값 : 20, 최소값 : 5
"""

# 입력받을 정수의 개수
count = 3
# 입력된 숫자들을 저장하기 위한 리스트 변수
numbers = []

for i in range(count) :
    input_num = int(input(f"{i+1}번째 정수 : "))
    numbers.append(input_num)

print(f"입력된 정수 리스트 : {numbers}")

# 리스트 객체는 정렬이 가능합니다.
# 리스트에 저장된 정수들을 오름차순으로 정렬함
numbers.sort()

# 오름차순으로 정렬된 리스트의 가장 앞 요소를
# 최소값으로 저장
min_value = numbers[0]
# 오름차순으로 정렬된 리스트의 가장 뒤 요소를
# 최대값으로 저장
#max_value = numbers[len(numbers) - 1]
max_value = numbers[-1]

# 합계 계산
total = 0
for data in numbers :
    total += data    

# 평균 계산
avg = total / len(numbers)

print(f"합계 : {total}, 평균 : {avg:.2f}, 최대값 : {max_value}, 최소값 : {min_value}")












