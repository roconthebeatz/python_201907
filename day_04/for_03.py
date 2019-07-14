# -*- coding: utf-8 -*-

# for 반복문은 정해진 횟수의 반복을 제어하는 경우에 효과적
# 특정 범위의 반복을 수행(리스트, 딕셔너리 ... 등의 크기만큼)

# for 변수명 in 컬렉션변수/값 : 
# 컬렉션 변수/값 내부의 데이터를 시작부터
# 끝까지 하나씩 추출하여 변수에 대입한 후 반복을 수행

# 리스트 타입의 컬렉션을 for 반복문으로 제어
numbers = list(range(1,11))
for data in numbers :
    print(f"data -> {data:2}")

# 딕셔너리 타입의 컬렉션을 for 반복문으로 제어
numbers = {"One" : 1, "Two" : 2, "Three" : 3, \
           "Four" : 4, "Five" : 5}

# 딕셔너리 타입의 컬렉션을 for문으로 반복하면
# 내부의 키 값들이 전달됩니다.
for key in numbers :
    print(f"key -> {key}")
    
    # 딕셔너리 타입의 변수에서 키 값을 사용하여
    # 값을 추출하는 코드
    # 1. [] 연산 : 반드시 존재하고 있는 키 값을 사용
    # - 만약 존재하지 않는 키 값인 경우 에러가 발생
    # 2. get 메소드
    # - 만약 존재하지 않는 키 값인 경우 None 값이 반환
    # - 에러 발생 X
    print(f"{key} -> {numbers[key]}")
    print(f"{key} -> {numbers.get(key)}")

# 딕셔너리 타입의 변수가 제공하는 items 메소드
# 딕셔너리 데이터들을 키와 값의 쌍으로 구성된 
# 리스트를 반환하는 메소드
# items 메소드를 사용하여 키와 값을 동시에 
# 전달받을 수 있음
for key, value in numbers.items() :
    print(f"{key} -> {value}")
    
# Set 타입의 컬렉션을 for 반복문으로 제어
# 아래의 msg Set 변수에는 문자의 중복이 제거된
# 값이 대입
msg = set("Hello Python~!")

for char in msg :
    print(f"char -> {char}")










































