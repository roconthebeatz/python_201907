# -*- coding: utf-8 -*-

# 문자열 포맷팅을 활용한 출력
# - 문자열 포맷팅 : 문자열 내부에 값 또는 변수를
#   사용하여 값을 채울 수 있는 방법

# 10 + 5 = 15
print("10 + 5 = 15")

# 출력에 사용할 변수 선언
n1 = 10.5654
n2 = 5.7798
r = n1 + n2

# 문자열 포맷팅을 사용한 출력 변수 생성
# - "포맷팅문자열" % (대입할 값 ...)
# - 포맷팅문자열 내부에 사용할 수 있는 서식
# - %d : 정수(십진수)
# - %f : 부동소수점(실수)
# - %s : 문자열
msg_1 = "%d %s %d = %d" % (n1, "+", n2, r)
print(msg_1)

msg_2 = "%5d %s %3d = %5d" % (n1, "+", n2, r)
print(msg_2)

msg_3 = "%-5d %s %-3d = %-5d" % (n1, "+", n2, r)
print(msg_3)

msg_4 = "%05d %s %03d = %05d" % (n1, "+", n2, r)
print(msg_4)

# 문자열의 format 메소드를 사용하여 정의하는 방법
# - "포맷팅문자열".format(값0 ...)
# - 값의 타입에 관계없이 위치 값(0부터시작)을 사용하여
#   출력할 수 있음
msg_5 = "{0} {1} {2} = {3}".format(n1, "+", n2, r )
print(msg_5)

msg_6 = "{0:.2f} {1} {2:.2f} = {3:.2f}".format(n1, "+", n2, r )
print(msg_6)

# 문자열의 fotmat 메소드를 개선한 포맷팅문자열 사용
# - 문자열의 선언부에 f를 지정
# - 문자열 내부의 {}를 사용하여 특정 변수, 값을 입력
# - fotmat 메소드의 선언없이 임의의 값을 채울 수 있음
# - 파이썬 3.6 이상에서만 가능함
msg_7 = f"{n1:.2f} {'+'} {n2:.2f} = {r:.2f}"
print(msg_7)
















