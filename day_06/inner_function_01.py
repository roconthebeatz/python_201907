# -*- coding: utf-8 -*-

# all, any 함수
# all 함수 : 매개변수로 전달된 컬렉션 내부의 모든 값이 True 인 경우
#            True 를 반환하는 함수 (and)
# any 함수 : 매개변수로 전달된 컬렉션 내부의 값이 하나라도 True 인 경우
#            True 를 반환하는 함수 (or)

# 파이썬 언어에서 True 를 의미하는 경우
# - 0, None, size(len함수의 결과)가 0이 아닌 경우
# - 문자열의 경우 None 이 아니거나 size(len함수의 결과)가 
# - 0이 아닌 경우

values = [1,2,3,4,5]
print(f"values -> {values}")
print(f"all(values) -> {all(values)}")
print(f"any(values) -> {any(values)}")

values = [1,2,3,0,5]
print(f"values -> {values}")
print(f"all(values) -> {all(values)}")
print(f"any(values) -> {any(values)}")

values = [1,2,3,"",5]
print(f"values -> {values}")
print(f"all(values) -> {all(values)}")
print(f"any(values) -> {any(values)}")

values = [1,2,3,None,5]
print(f"values -> {values}")
print(f"all(values) -> {all(values)}")
print(f"any(values) -> {any(values)}")

# 거짓을 의미하는 데이터의 모음
values = [0,"",None,[],False]
print(f"values -> {values}")
print(f"all(values) -> {all(values)}")
print(f"any(values) -> {any(values)}")





