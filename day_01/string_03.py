# -*- coding: utf-8 -*-

# 파이썬의 슬라이싱 연산
# 배열/리스트/문자열에 사용할 수 있는 연산
# 인덱스 정보를 기반으로 임의의 지점에 값들을 추출할 수 있음
# - 변수명[시작인덱스 : 종료인덱스]
# - 시작인덱스부터 시작하여 종료인덱스 -1 번째 값들이 반환

msg = "Hello Python~!"
print(msg)

# msg 문자열 변수(Hello Python~!) 에서
# Python 문자열을 추출하는 슬라이싱 연산 예제
msg_part = msg[6:12]
print(msg_part)

# msg 문자열 변수(Hello Python~!) 에서
# Hello 문자열을 추출하는 슬라이싱 연산 예제
msg_part = msg[0:5]
print(msg_part)

# 슬라이싱 연산 시, 시작위치부터 (0 인덱스) 추출하는 경우
# 0은 생략할 수 있습니다.
msg_part = msg[:5]
print(msg_part)

# 특정 위치에서 마지막 요소까지 슬라이싱을 하는 경우
# 종료인덱스는 생략할 수 있습니다.
# msg 문자열 변수(Hello Python~!) 에서
# Python~! 문자열을 추출하는 슬라이싱 연산 예제
msg_part = msg[6:]
print(msg_part)

# 슬라이싱 연산에서도 -1 인덱스를 활용할 수 있음
# msg 문자열 변수(Hello Python~!) 에서
# Hello Python~ 문자열을 추출하는 슬라이싱 연산 예제
msg_part = msg[:-1]
print(msg_part)

# - 인덱스는 배열 또는 리스트의 뒤부분부터 인덱스를
# 지정하는 방법
# -2 인덱스는 마지막에서 2번째 위치한 요소의 인덱스
msg_part = msg[:-2]
print(msg_part)



















