# -*- coding: utf-8 -*-

# 구구단의 실행 결과를 저장하는 리스트를 생성하세요.
# EX) [2,4,6,8,10,12,14,16,18,3,6,9...81]

# 구구단의 실행 결과를 저장하는 리스트 변수
#result = []
#for dan in range(2,10) :
#    for mul in range(1,10) :
#        result.append(dan * mul)

# 리스트 변수의 선언에 중첩된 for문이 활용되는 예제
# 리스트변수명 = [실행문 외부의 for문 내부의 for문]
result = [dan * mul for dan in range(2,10) 
            for mul in range(1,10)]

print(result)