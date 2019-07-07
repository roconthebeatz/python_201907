# -*- coding: utf-8 -*-

# 리스트에 데이터를 추가하는 방법
# 1. append 메소드를 사용
# - 기본적으로 리스트의 가장 마지막 요소로 추가
numbers = [1,3,5]
print(numbers)

# numbers 리스트의 마지막 요소로 7 추가
numbers.append(7)
print(numbers)

# numbers 리스트의 8과 9 추가
# append 메소드는 매개변수로 1개를 입력받기 때문에
# 아래의 append 메소드 실행은 에러가 발생됩니다.
# numbers.append(8,9)

# 아래와 같이 리스트를 추가하는 경우 하위 리스트로
# 추가됩니다.
numbers.append([8,9])
print(numbers)

numbers.pop()
print(numbers)

# 다수개의 데이터를 리스트의 마지막에 추가하는 경우
# + 연산자를 사용한 결합 연산을 활용합니다.
numbers = numbers + [8,9]
print(numbers)

# 리스트의 특정 인덱스 위치로 값을 추가하는 경우
# insert 메소드를 사용할 수 있습니다.
# 리스트변수명.insert(추가할위치의인덱스, 추가할 값)
numbers.insert(1, 2)
print(numbers)

numbers.insert(3, 4)
print(numbers)

numbers.insert(5, 6)
print(numbers)

















