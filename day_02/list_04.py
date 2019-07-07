# -*- coding: utf-8 -*-

# 파이썬의 모든 변수들은 객체를 참조하는 방식을 사용합니다.
# (실제 데이터를 저장하는 방식이 아닌 주소값(참조값)을 저장)

numbers = [1, 2, 3, 4, 5]
print(f"numbers -> {numbers}")

# 아래의 numbers_copy 변수는 새로운 리스트를 할당받지 않고
# 기존의 numbers 변수가 참조하고 있는 리스트를 공유하는
# 변수가 됩니다.
numbers_copy = numbers
print(f"numbers -> {numbers}")
print(f"numbers_copy -> {numbers_copy}")

# numbers_copy 변수를 사용하여 리스트 내부의 값을 수정하면
# 기존의 numbers 변수를 사용해서도 변경된
# 값을 확인할 수 있습니다.
# 얕은복사현상 : 실제 데이터가 복사되지 않고, 
# 참조값만 공유되는 현상
numbers_copy[0] = 100
print(f"numbers -> {numbers}")
print(f"numbers_copy -> {numbers_copy}")

# 리스트 데이터의 복제를 위한 슬라이싱 연산
# (주소값을 전달하는 방식이 아닌 실제 데이터를 복사하여 전달)
numbers_copy = numbers[:]

numbers_copy[1] = 200
print(f"numbers -> {numbers}")
print(f"numbers_copy -> {numbers_copy}")

















