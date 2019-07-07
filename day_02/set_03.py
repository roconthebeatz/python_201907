# -*- coding: utf-8 -*-

# Set 타입에 데이터를 추가하는 방법
# 1. add 메소드를 사용하여 추가하는 방법
# - 하나의 값을 Set 내부에 추가

# 비어있는 Set 변수를 생성
numbers = set()
print(f"numbers's size -> {len(numbers)}")

# add 메소드를 사용하여 데이터를 추가
# 순차적으로 add 메소드가 실행될 때 마다
# 저장되는 데이터의 개수가 증가되는 것을 확인
numbers.add(10)
print(f"numbers's size -> {len(numbers)}")
numbers.add(11)
print(f"numbers's size -> {len(numbers)}")
numbers.add(12)
print(f"numbers's size -> {len(numbers)}")
numbers.add(13)
print(f"numbers's size -> {len(numbers)}")

# 중복된 데이터는 추가되지 않습니다.
numbers.add(13)
print(f"numbers's size -> {len(numbers)}")

print(numbers)

# 2. Set 타입의 update 메소드를 사용하여
# 다수개의 데이터를 추가할 수 있음
numbers.update([14,15,16,17,18,19])

print(f"numbers's size -> {len(numbers)}")
print(numbers)























