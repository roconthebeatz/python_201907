# -*- coding: utf-8 -*-

messages = ["Hello", "Index", "Python", "Hi"]

# messages 리스트 내부의 데이터 중, 첫 글자가 H 인 데이터만
# 추출하는 코드 (새로운 리스트로 생성)

# 반복문과 조건식을 활용한 방법
#result = []
#for data in messages :
#    if data[0] == "H" :
#        result.append(data)

# 함수를 사용하여 조건식을 비교한 후, True/False의 값을 반환
#def checkH(data) :
#    if data == "H" :
#        return True
#    else :
#        return False
#    
#result = []
#for data in messages :
#    if checkH(data[0]) :
#        result.append(data)

# 조건의 결과 반환 함수와 filter 함수를 조합하여 사용하는 방법
#def checkH(data) :
#    if data[0] == "H" :
#        return True
#    else :
#        return False
#    
#result = list(filter(checkH, messages))

# lambda와 filter 함수를 조합하여 사용하는 방법
# lambda : 특정 매개변수를 전달받아 값을 반환하는 함수를 정의
# lambda 매개변수 ... : 반환식
result = list(filter(lambda data : data[0] == "H", messages))
print(result)
# lambda 변수는 함수와 같이 활용할 수 있습니다.
plus = lambda n1, n2 : n1 + n2
print(f"plus(11, 7) -> {plus(11, 7)}")

# 아래의 numbers 리스트에서 3의 배수만 추출한 리스트를
# 생성한 후, 화면에 결과를 출력하세요.
numbers = [22,23,11,15,17,90,33]

#def check3(data) :
#    return data % 3 == 0
#
#result = list( filter(check3, numbers) )

result = list( filter( lambda data : data % 3 == 0, numbers ) )
print(result)











