# -*- coding: utf-8 -*-

# Set 타입 내부의 데이터 삭제
# - remove, pop 메소드를 사용
numbers = set([1,2,3,4,5,6,7,8,9])

# 1. remove 메소드 사용
# - 특정 데이터를 삭제하는 경우 사용
# - 삭제만 수행(삭제된 값을 반환하지 않음)
numbers.remove(5)
print(numbers)

r_value = numbers.remove(8)
print(numbers)
# remove 메소드는 삭제한 결과를 반환하지 않으므로
# r_value 에는 None 값이 대입됩니다.
print(f"r_value -> {r_value}")

# Set 내부에 저장되어 있지 않은 값은 삭제할 수 없음
# (에러가 발생됨)
numbers.remove(0)

# 2. pop 메소드를 사용하여 데이터를 삭제
# - 가장 앞에 위치한 데이터를 삭제할 때 사용
# - Set 내부에서 가장 앞에 위치한 데이터를 삭제하고
#   삭제한 값을 반환
r_value = numbers.pop()
print(numbers)
print(f"r_value -> {r_value}")

# 3. clear 메소드를 사용
# - Set 내부의 모든 데이터를 삭제
numbers.clear()
print(numbers)



















