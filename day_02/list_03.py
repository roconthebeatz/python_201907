# -*- coding: utf-8 -*-

# 리스트 내부 요소의 값 수정

# 문자열 데이터와 같은 경우 배열(리스트)의 형태로 저장되며
# 값의 수정이 허용되지 않는 데이터 타입입니다.
msg = "Hello Python~!"
msg[0] = 'h'

# 반면, 일반적인 리스트 변수는 내부 요소의 값을
# 수정할 수 있습니다.
numbers = [1,2,3,4,5]
print(f"before : {numbers}")
numbers[2] = 3.3
print(f"after : {numbers}")












