# -*- coding: utf-8 -*-

# 리스트 내부에 저장된 요소들을 정렬하는 방법
# - sort 메소드를 사용하여 처리할 수 있음
numbers = [5,1,3,2,9,6,7,8]
print(numbers)

# 리스트 내부의 요소들을 오름차순 정렬하는 예제
# sort 메소드 사용
numbers.sort()
print(numbers)

# sort 메소드의 reverse 매개변수의 값을 True로
# 지정하여 내림차순 정렬을 수행할 수 있음
numbers.sort(reverse=True)
print(numbers)

# 리스트 변수의 reverse 메소드를 사용하여
# 정렬된 이후, 역순으로 값을 배치할 수 있음
numbers.reverse()
print(numbers)
























