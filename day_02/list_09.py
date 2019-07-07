# -*- coding: utf-8 -*-

# 리스트 내부에 저장된 데이터를 검색하는 방법

# index 메소드를 사용하여 처리할 수 있음
numbers = [1,2,3,4,5,6,7,8,9]

# index 메소드는 매개변수로 전달된 값이 저장되어 있는
# 인덱스 값을 반환합니다.
target = 7
target_index = numbers.index(target)
print(f"{target} 데이터는 {target_index} 위치에 저장되어 있습니다.")

# index 메소드는 리스트 내부에서 검색할 값을 
# 찾지못한 경우 에러가 발생됩니다.
target = 0
target_index = numbers.index(target)
print(f"{target} 데이터는 {target_index} 위치에 저장되어 있습니다.")

# 리스트 변수는 count 메소드를 제공하며
# count 메소드를 통해서 특정 데이터가 
# 리스트 내부에 저장된 개수를 확인할 수 있습니다.
target = 5
target_count = numbers.count(target)
print(f"{target} 데이터는 {target_count} 개 저장되어 있습니다.")

# 리스트 변수의 count 메소드를 사용하여 
# 매개변수의 저장 여부를 확인한 이후,
# index 메소드를 사용하여 위치를 확인할 수 있습니다.
# - 만약 count 메소드의 결과가 0 인 경우
#   index 메소드를 사용하면 에러가 발생
target = 0
target_count = numbers.count(target)
print(f"{target} 데이터는 {target_count} 개 저장되어 있습니다.")

















