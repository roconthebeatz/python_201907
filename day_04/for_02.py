# -*- coding: utf-8 -*-

# for 반복문
# for 변수명 in 컬렉션타입의 변수 / 데이터 :
#   반복해서 실행할 문장
#   (컬렉션 내부에서 데이터를 하나씩 추출하여 작업할 내용)

# for 반복문은 지정된 횟수의 반복을 제어할 때 효과적
# (특정 컬렉션의 개수만큼 반복을 처리하는 경우가 대다수)

# for 문에서 가장 많이 활용되는 함수
# range 함수 - 특정 값의 영역에 해당되는 리스트를 반환
# range(5) -> range(0, 5)
# list(range(5)) -> [0, 1, 2, 3, 4]

# range 함수의 사용방법
# 1. 매개변수가 1개인 경우
# - range(STOP)
# - range(5) -> [0, 1, 2, 3, 4]

# 2. 매개변수가 2개인 경우
# - range(START, STOP)
# - range(2, 5) -> [2, 3, 4]

# 3. 매개변수가 3개인 경우
# - range(START, STOP, STEP)
# - range(1, 10, 2) -> [1, 3, 5, 7, 9]

# range 함수를 적용한 for 반복문

for i in range(10) :
    print(f"i -> {i:2}")

for i in range(5, 10) :
    print(f"i -> {i:2}")

for i in range(1, 10, 2) :
    print(f"i -> {i:2}")

# 1 에서 100 까지 정수들의 합계를 계산하여 출력하세요.
total = 0
for i in range(1, 101) :
    #print(i)
    total += i

print(f"1 에서 100 까지 정수들의 합계 : {total}")













