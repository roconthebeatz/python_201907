# -*- coding: utf-8 -*-

# 제어문의 중첩된 사용
# 제어문들은 서로 다른 제어문에 포함될 수 있음

# 1 ~ 100 까지의 정수를 출력하세요.
# (홀수만 출력하세요...)

step = 1

while step < 101 :
    if step % 2 == 1 :
        # 제어문 내부에 위한 또다른 제어문의
        # 실행 코드는 해당 제어문의 영역에 
        # 포함되기 위해서
        # 추가적으로 들여쓰기를 작성해야 합니다.
        print(f"step => {step:3}")
        
    step += 1
    
print("프로그램 종료")








