# -*- coding: utf-8 -*-

# 반복문과 else 구문
# - 반복문과 else 구문이 결합될 수 있음
# - else 구문은 반복이 종료되는 지점에 정의하며
#   반복문의 조건식이 False가 되는 시점에
#   실행됩니다.

step = 1

while step < 11 :
    print(f"step -> {step:2}")
    step += 1
else :
    # 위의 while 반복문의 조건식이 False가
    # 되어 반복이 중료되면 호출되는 else 구문
    # (반복문이 정상적으로 종료되었음을 의미)
    print("while 반복문이 종료됨")
    
print("프로그램 종료")
    







