# -*- coding: utf-8 -*-

# 제어문 - 반복문
# 특정 영역에 위치한 실행문들을 
# 조건식의 결과에 따라 반복할 수 있는 문법
# (조건식의 결과가 거짓이 될 때까지 반복)
# - while, for

# while 반복문
# while 조건식 :
#   반복해서 실행할 문장

step = 1

while step <= 10 :
    print(f"step -> {step:2}")
    
    # 반복문을 종료하기 위한 step 변수의 값 수정
    # step 변수에 자기자신의 값 + 1의 값을 대입
    #step = step + 1
    
    # 변형된 형태의 대입 연산자
    # 자기 자신에 연산한 결과를 대입받을 때 사용함
    # 아래의 코드는 step = step + 1 과 동일한 코드
    step += 1
   
print("프로그램 종료")
print(f"반복의 종료 후, step -> {step:2}")
















