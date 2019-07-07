# -*- coding: utf-8 -*-

# variable_01.py

# 변수
# 임의의 메모리 공간(RAM)에 이름을 할당하여 관리하는 방법
# 변수를 활용하여 RAM 공간을 활용할 수 있음

# 변수를 생성하는 방법
# - 파이썬에서는 정적 타입의 변수가 아닌 
#   동적 타입의 변수를 지원함
# - 정적 타입 : 데이터의 형태가 고정된 변수(정수,실수,문자열)
# - 동적 타입 : 변수의 생성 이후, 
#              값이 대입될 때 타입이 결정되는 변수

# 변수명(식별자) = 값

# 식별자의 규칙
# 첫 글자는 영문자로 작성하되 ( _ 도 사용가능함)
# 두번째 글자 이후부터는 숫자도 가능
# 주의사항
# 파이썬에서 이미 사용중인 키워드는 사용할 수 없음
# - if, for ...

number = 15
print(f"number : {number}")
print(f"number : {type(number)}")

# 파이썬의 변수는 타입이 동적으로 처리되기 때문에
# 초기값과 다른 타입의 값을 대입할 수 있습니다.
number = 107.557
print(f"number : {number}")
print(f"number : {type(number)}")

number = "11.751"
print(f"number : {number}")
print(f"number : {type(number)}")











