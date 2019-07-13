# -*- coding: utf-8 -*-

# 중첩된 구조의 반복문
# - 반복문 내부에 반복문이 정의되는 형태
# - 외부의 반복문이 1번 실행될 때,
#   내부의 반복문은 전체를 실행합니다.

step_out = 1
while step_out <= 3 :
    
    step_in = 1
    while step_in <= 3 :
        print(f"out : {step_out}, in : {step_in}")
        step_in += 1
        
    step_out += 1
    
print("프로그램 종료")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    