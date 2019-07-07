# -*- coding: utf-8 -*-

# 딕셔너리 변수 내부에 저장된 데이터를 삭제하는 방법
numbers = { "ONE" : 1, "TWO" : 2, "THREE" : 3 }
print(numbers)
print(len(numbers))

# del 연산자를 사용하여 딕셔너리 내부의 데이터를 삭제
# - 키 값이 사용됨
# - del 딕셔너리변수[삭제할키값]
del numbers["TWO"]
print(numbers)
print(len(numbers))

# del 연산자를 사용하여 데이터를 삭제할 때
# 딕셔너리에 저장되지 않은 키 값을 사용하는 경우
# 에러가 발생됨
del numbers["ZERO"]

# 딕셔너리 내부의 데이터를 삭제하기 이전에
# 키 값의 존재 여부를 확인하는 방법
# - in 연산자를 사용하여 처리
# - 검색할키값 in 딕셔너리변수명
# - 검색할 키 값이 존재하는 경우 True
#   존재하지 않는 키 값인 경우 False
isThree = "THREE" in numbers
print(f"isThree -> {isThree}")

isFive = "FIVE" in numbers
print(f"isFive -> {isFive}")

# 딕셔너리 변수 내부의 모든 데이터를 삭제하는 방법
# - clear 메소드를 사용
print(numbers)

numbers.clear()
print(numbers)
print(len(numbers))



















