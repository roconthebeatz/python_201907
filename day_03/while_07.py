# -*- coding: utf-8 -*-

# 반복문과 continue 키워드
# 반복문 내부에서 continue 키워드는
# 현재의 실행을 중지하고 다음 반복으로
# 이동하기 위해서 사용되는 키워드
# (반복을 종료하는 것이 아님)
# (반복문의 종료 지점으로 이동하여
#  다음 반복이 실행되도록 제어하는 키워드)

# 1 ~ 100까지의 정수 중, 짝수만 출력하세요.
step = 1
while step < 101 :
    # 홀수인 경우에는 반복문의 내용을 실행하지
    # 않고 건너뜀
    if step % 2 == 1 :
        step += 1
        continue
    
    #  짝수인 경우 실행을 위한 제어문
#    if step % 2 == 0 :
#        print(f"step -> {step:3}")
    
    print(f"step -> {step:3}")        
    step += 1
    
print("프로그램 종료")