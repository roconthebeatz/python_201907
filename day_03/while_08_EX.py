# -*- coding: utf-8 -*-

# 사용자에게 정수 10개를 입력받아
# 입력된 정수의 목록을 출력한 후,
# 입력된 정수들의 총 합계와 평균,
# 최대값, 최소값을 출력하세요.

# 1. 입력
count = 10
numbers = list()

while len(numbers) < count :
    value = input(f"{len(numbers) + 1}번째 정수 : ")
    value = value.strip()
    if value == "" :
        continue
    
    numbers.append(int(value))
    
# 2. 처리 - 합계와 평균, 최대값, 최소값
# 최대값과 최소값의 경우 현재 데이터 중의 값을
# 계산해야하므로, 입력된 리스트의 첫번째 값으로
# 초기화를 진행함
max_value = min_value = total = numbers[0]

step = 1
while step < count :
    total += numbers[step]
    
    if max_value < numbers[step] :
        max_value = numbers[step]
            
    if min_value > numbers[step] :
        min_value = numbers[step]
        
    step += 1

avg = total / count

# 3. 출력
print(f"입력된 요소의 값 : {numbers}")
print(f"총점 : {total}, 평균 : {avg:.2f}")
print(f"최대값 : {max_value}, 최소값 : {min_value}")















