# -*- coding: utf-8 -*-

# 논리연산자
# 다수개의 관계식의 결과(진리형값)를
# 하나의 진리형의 결과로 반환할 수 있는 연산자

# 1. and 연산자
"""
AND 연산자의 진리표
좌항    우항    and결과
FALSE   FALSE  FALSE
FALSE   TRUE   FALSE
TRUE    FALSE  FALSE
TRUE    TRUE   TRUE
"""
print("{} {} {} = {}".format(
        False, "and", False, False and False))
print("{} {} {} = {}".format(
        False, "and", True, False and True))
print("{} {} {} = {}".format(
        True, "and", False, True and False))
print("{} {} {} = {}".format(
        True, "and", True, True and True))

# 2. or 연산자
"""
OR 연산자의 진리표
좌항    우항    or결과
FALSE   FALSE  FALSE
FALSE   TRUE   TRUE
TRUE    FALSE  TRUE
TRUE    TRUE   TRUE
"""
print("{} {} {} = {}".format(
        False, "or", False, False or False))
print("{} {} {} = {}".format(
        False, "or", True, False or True))
print("{} {} {} = {}".format(
        True, "or", False, True or False))
print("{} {} {} = {}".format(
        True, "or", True, True or True))

# 3. not 연산자
# - 단항 연산자
# - not (관계식 또는 진리형값)
# - 우항의 값을 부정한 결과를 반환
# not False -> True
# not True -> False

print("not {} = {}".format(False, not False))
print("not {} = {}".format(True, not True))

# 연습 예제

# - 성별의 정보를 저장하고 있는 변수
# - (1, 3) : 남성, (2, 4) : 여성
gender = 2

# 문제 1. gender 변수이 값을 사용하여
# 남성 여부의 값을 진리형으로 출력하세요.
result_1 = gender == 1 or gender == 3
print(f"문제 1 : {result_1}")

# - 나이의 정보를 저장하고 있는 변수
age = 25

# 문제 2. age 변수이 값을 사용하여
# 20대 또는 30대인 경우를 판단하여 
# 진리형으로 출력하세요.

# - age 변수의 값의 범위를 사용하여 판단하는 예제
#result_2 = (age >= 20 and age < 30) or (age >= 30 and age < 40)

# - age 변수에 10의 자리수를 추출하여 판단하는 예제
# (/ 연산을 사용하면 소수점이하까지 계산되므로
# // 연산을 사용하여 정수의 값만을 추출합니다.)
result_2 = (age // 10 == 2) or (age // 10 == 3)
print(f"문제 2 : {result_2}")

# 문제 3. 성별이 여자이고, 나이가 20대인 경우를
# 판단하여 진리형으로 출력하세요.

# 한 줄의 실행 코드로 진리형 값을 반환받는 코드
#result_3 = (gender == 2 or gender == 4) and (age // 10 == 2)

# 각 조건을 별도의 변수로 저장하여 처리하는 코드
# - 성별 판단의 결과를 저장
result_3_gender = (gender == 2 or gender == 4)
# - 나이 판단의 결과를 저장
result_3_age = (age // 10 == 2)
# - 최종 결과를 생성
result_3 = result_3_gender and result_3_age

print(f"문제 3 : {result_3}")

























