# -*- coding: utf-8 -*-

# 문자열에 적용할 수 있는 함수 또는 메소드

msg = "Hello Python~!"

# 문자열의 길이를 확인할 수 있는 함수
# len 함수를 사용
# (문자열뿐만 아니라 
# 배열/리스트의 개수도 확인할 수 있음)
size = len(msg)
print(f'msg 변수는 {size} 글자로 작성되었습니다.')

# 특정 문자열의 위치(인덱스) 확인
# 파이썬의 문자열 값 또는 변수는 find 메소드를 제공
# 문자열변수/값.find("검색할문자열값")
# - 검색할 문자열의 시작인덱스 값이 반환
find_index = msg.find("Python")
print(f"msg 변수에서 'Python'의 위치는 \
{find_index} 입니다.")

# 문자열의 공백 제거(엔터키, 띄어쓰기, 탭)
# \n : 엔터키(개행문자)
# \t : 탭키
msg = "\t\tHello Python~!\n"
print(msg)
print(msg)

# lstrip 메소드 : 문자열의 왼쪽 공백을 제거
print(f"lstrip : {msg.lstrip()}")
# rstrip 메소드 : 문자열의 오른쪽 공백을 제거
print(f"rstrip : {msg.rstrip()}")
# strip 메소드 : 문자열의 좌우 공백을 제거
print(f"strip : {msg.strip()}")

# lstrip, rstrip, strip 메소드의 추가 기능
# 기본적으로 공백을 제거할 수 있는 기능을 제공하며
# 만약 메소드의 매개변수를 전달하는 경우
# 해당 매개변수의 값을 문자열에서 제거할 수 있습니다.
msg = "Hello Python~!"

print(f"lstrip : {msg.lstrip('eHl')}")
print(f"rstrip : {msg.rstrip('eHl')}")
print(f"strip : {msg.strip('eHl')}")

# 문자열 데이터를 변경한 후 결과를 반환받는 방법
# replace 메소드
# 문자열값/변수.replace("기존문자열", "변경할문자열")
# 주의사항!
# - 원본 문자열은 수정되지 않음
# - 수정된 문자열이 반환됨
msg = "Hello Java~!"
msg_replace = msg.replace("Java", "Python")
print(f"변경 전 : {msg}\n변경 후 : {msg_replace}")

# 문자열 데이터를 특정 문자열값을 기준으로 분할하는 방법
# split 메소드
# 문자열변수/값.split() -> 공백을 기준으로 분할
# 문자열변수/값.split(",") -> , 를 기준으로 분할
subjects = "KOR ENG MATH"
# split 메소드에 의해서 공백을 기준으로 분할된 후
# 다수개의 데이터를 저장하는 리스트 타입으로 반환됨
subjects_split = subjects.split()
print(f"분할된 결과 : {subjects_split}")

scores = "99;80;85"
scores_split = scores.split(';')
print(f"분할된 결과 : {scores_split}")

jumin = "990120-2012521"

# 문제 1
# 위의 jumin 변수에서 생년월일에 해당되는 정보를 추출하세요.
# EX) 99년 1월 20일생 입니다.

# - 주민번호에서 생년월일에 해당되는 정보를 추출
# - split 메소드의 첫번째 반환값을 추출
#   (인덱스 연산 사용)
birth = jumin.split('-')[0]
year = birth[:2]
month = birth[2:4]
day = birth[-2:]

print(f"{year}년 {month}월 {day}일생 입니다.")





















