# -*- coding: utf-8 -*-

# 리스트 데이터에 대한 슬라이싱 연산
# 리스트 내부의 특정 영역 데이터를 복제하는 연산
# 리스트변수명[시작인덱스:종료인덱스]
numbers = [1,2,3,4,5,6,7,8,9]
numbers_part = numbers[2:7]

print(numbers)
print(numbers_part)

# 슬라이싱을 통해서 추출된 데이터는
# 완전 복제로 처리되어 수정하는 경우에도 
# 원본데이터는 영향이 없음
numbers_part[0] = 300
print(numbers)
print(numbers_part)