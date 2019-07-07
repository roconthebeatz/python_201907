# -*- coding: utf-8 -*-

# 리스트의 데이터 수정 및 삭제
# - 리스트 내부의 데이터 수정은 인덱스 정보를
# 사용하여 처리할 수 있음

numbers = [1,2,3,4,5]
print(numbers)

# 인덱스 연산을 사용하여 값을 수정하는 예제
numbers[3] = 40
print(numbers)

# 인덱스 연산을 사용하여 하위 리스트를 
# 추가할 수 있습니다.
numbers[3] = [41,42,43]
print(numbers)

# 슬라이싱 연산을 사용하여 리스트 내부의
# 데이터를 수정하는 방법
# - 슬라이싱 연산을 하는 경우
#   하위 리스트가 대입되는 것이 아닌
#   요소들이 대입됩니다.
numbers[2:4] = [41,42,43]
print(numbers)

# 리스트 내부의 요소를 삭제하는 방법
# del 연산자 사용
# del 리스트변수명[삭제할인덱스]
del numbers[5]
print(numbers)

# del 리스트변수명[삭제할시작인덱스:종료인덱스]
del numbers[2:]
print(numbers)

numbers = [1,2,3,4,5]

# 리스트의 메소드를 활용한 삭제 방법
# remove, pop 메소드

# 리스트에 저장되어 있는 값을 기준으로
# 삭제하는 방법
# - 리스트 내부에 저장된 3을 삭제하는 예제
numbers.remove(3)
print(numbers)

# remove 메소드는 최초에 발견된 위치의 데이터만
# 삭제하고 남은 데이터는 삭제하지 않음
numbers = [1,2,3,4,5,3]
numbers.remove(3)
print(numbers)

# pop 메소드
# - 리스트의 가장 마지막 데이터를 
# 삭제할 수 있는 메소드
numbers = [1,2,3,4,5,3]
numbers.pop()
print(numbers)

# pop 메소드는 리스트의 마지막 요소를 삭제하면서
# 삭제한 값을 반환하는 메소드입니다.
pop_data = numbers.pop()
print(f"pop 메소드에 의해서 삭제된 값 : {pop_data}")

















