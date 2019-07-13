# -*- coding: utf-8 -*-

# 사용자로부터 5개의 정수를 입력받아
# 입력된 모든 정수의 합계를 출력하세요

# 1. 입력
numbers = []

step = 0
while step < 5 :
    numbers.append(
            int(input(f"{step+1}번째 정수를 입력하세요 : ")))
    step += 1

# 2. 처리
total = 0
step = 0
while step < len(numbers) :
    total += numbers[step]
    step += 1
    
# 3. 출력
print(f"입력된 값 : {numbers}")
print(f"합계 : {total}")














