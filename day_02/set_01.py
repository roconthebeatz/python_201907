# -*- coding: utf-8 -*-

# Set 타입의 데이터
# - 내부의 데이터 중복을 허용하지 않는 타입
# - 딕셔너리와 차이점은 키 값이 존재하지 않음
# - 내부에 저장된 데이터의 저장 순서를 유지하지 않음

# 생성 방법
# - 비어있는 Set 타입의 변수 생성
# - 변수명 = set()
# - 초기값이 있는 Set 타입의 변수 생성
# - 변수명 = set(초기값으로 지정할 데이터)
set_01 = set()
print(f"set_01's type -> {type(set_01)}")
print(f"set_01's size -> {len(set_01)}")

set_02 = set([1,2,3])
print(f"set_02's type -> {type(set_02)}")
print(f"set_02's size -> {len(set_02)}")

# 중복된 값이 허용되지 않는 것을 확인할 수 있음
set_03 = set([1,2,3,1,2,3])
print(f"set_03's type -> {type(set_03)}")
print(f"set_03's size -> {len(set_03)}")

# Set 타입에 문자열 데이터를 저장할 수 있음
# - 해당 문자열 구성하는 각 문자값들이 저장됨
# - 중복은 제거되며, 순서가 유지되지 않음
set_04 = set("Hello Python")
print(f"set_04's size -> {len(set_04)}")
print(f"set_04 -> {set_04}")














