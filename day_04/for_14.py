# -*- coding: utf-8 -*-

# 구구단의 실행 결과를 저장하는 리스트를 생성하세요.
# (홀수단에 해당되는 결과만 저장)

#result = []
#for dan in range(2,10) :
#    
#    if dan % 2 == 0 :
#        continue
#    
#    for mul in range(1,10) :
#        result.append(dan * mul)

# 리스트 변수의 선언에 중첩된 반복문이 사용되는 예제
# (외부/내부 반복문에 조건식을 적용하려는 경우)
# 리스트변수명 = 
# [실행문 실행문의if문 else '조건식이 거짓일 경우 실행할 문장'
# '외부의 for문' '외부의 for문이 실행될 때 적용할 if문'
# '내부의 for문' '내부의 for문이 실행될 때 적용할 if문']
result = [dan * mul if dan * mul > 10 else 0
          for dan in range(2,10) if dan % 2 == 1
          for mul in range(1,10) if dan % 2 == mul % 2 ]
        
print(result)


















