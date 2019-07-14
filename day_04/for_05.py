# -*- coding: utf-8 -*-

# 중첩된 구조의 반복문을 사용하여
# 구구단을 출력하세요
# - while문을 사용한 구구단

# 외부의 반복문 조건에 사용할 변수(단수제어)
step_outer = 2
while step_outer < 10 :
    
    print(f"{step_outer}단을 출력합니다.")
    
    # 내부의 반복문 조건에 사용할 변수(곱해지는수)
    step_inner = 1
    while step_inner < 10 :
        print(f"{step_outer} * {step_inner} = {step_outer * step_inner}")
        # 내부의 반복문을 종료하기 위한
        # 변수 제어
        step_inner += 1
        
    # 외부의 반복문을 종료하기 위한
    # 변수 제어
    step_outer += 1
    
# - for문을 사용한 구구단
for step_outer in range(2, 10) :
    
    print(f"{step_outer}단을 출력합니다.")
    
    for step_inner in range(1, 10) : 
        
        print(f"{step_outer} * {step_inner} = {step_outer * step_inner}")
        
















        
        
        
        
        
        
        
        
        
        
        