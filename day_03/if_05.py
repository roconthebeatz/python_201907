# -*- coding: utf-8 -*-

# 조건식이 다수개인 경우의 처리방법
# if ~ elif ~ else
# if 1번째 조건식 :
#   1번째 조건식이 참일 경우 실행할 문장
# elif 2번째 조건식 :
#   2번째 조건식이 참일 경우 실행할 문장
# ...
# elif N번째 조건식 :
#   N번째 조건식이 참일 경우 실행할 문장
# else :
#   모든 조건식이 거짓일 경우 실행할 문장

print("1. 한식")
print("2. 일식")
print("3. 중식")
menu = int(input('메뉴를 선택하세요 : '))

output = None
if menu == 1 :
    output = "오늘 한식 메뉴는 김치찌개입니다."
elif menu == 2 :
    output = "오늘 일식 메뉴는 돈까스입니다."
elif menu == 3 :
    output = "오늘 중식 메뉴는 짜장면입니다."
else :
    output = "1 ~ 3번 까지의 메뉴만 존재합니다."
    
print(output)









