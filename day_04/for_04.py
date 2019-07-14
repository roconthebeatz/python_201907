# -*- coding: utf-8 -*-

# 중첩된 반복문
# - 반복문 내부에 하위 반복문이 선언되는 형태
# - 외부의 반복문이 한번 실행될 때,
#   내부의 반복문은 전체가 실행됩니다.

for outer in range(1,4) :
    
    for inner in range(1,4) :
        
        print(f"outer : {outer}, inner : {inner}")
        
print("프로그램 종료")