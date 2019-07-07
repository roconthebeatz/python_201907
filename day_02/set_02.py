# -*- coding: utf-8 -*-

# Set 타입 내부의 데이터 접근방법

# Set 타입은 기본적으로 데이터의 직접 접근을
# 허용하지 않습니다.

# Set 타입에 저장된 데이터는 리스트 타입으로
# 변환할 수 있으며, 리스트로 변환된 이후
# 인덱스 연산을 사용하여 값에 접근할 수 있음

# Set 타입의 변수 생성
msg_set = set("Hello Python~!")

# Set 타입의 변수를 리스트 타입으로 변환
# - list(set변수명)
msg_list = list(msg_set)

print(msg_set)
print(msg_list)

# List 타입으로 변환되 이 후,
# 인덱스를 사용하여 값에 접근할 수 있음
print(f"msg_list[0] -> {msg_list[0]}")
print(f"msg_list[-1] -> {msg_list[-1]}")




















