# -*- coding: utf-8 -*-

# sort 메소드를 이용하지 않고
# 리스트의 오름차순 정렬을 구현하세요.

numbers = [3, 5, 1, 7, 2]

# 정렬의 기준 인덱스를 정하는 외부의 반복문
for i in range(len(numbers) - 1) : 
    # 기준 인덱스 위치의 값 다은 위치부터 
    # 마지막 위치까지 값을 비교하기 위한 내부의 반복문
    for j in range(i+1, len(numbers)) :
        
        # 오름차순 정렬이므로, i번째 위치의 값은
        # j번째 위치의 값보다가 항상 작아야함
        # 만약 j번째 위치값이 더 작다면
        # i번째와 j번째 위치값을 서로 교환함
        if numbers[i] > numbers[j] :
            # 일반적인 두 변수의 값을 교환하기 위한
            # SWAP로직
#            temp = numbers[i]
#            numbers[i] = numbers[j]
#            numbers[j] = temp
            
            # 파이썬 언어에서 사용할 수 있는
            # SWAP 코드
            numbers[i], numbers[j] = numbers[j], numbers[i]
            
print("정렬 결과 : ", numbers)            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            