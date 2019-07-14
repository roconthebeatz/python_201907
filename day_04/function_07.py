# -*- coding: utf-8 -*-

# 가변매개변수를 사용하는 경우의 주의사항

# 연산에 사용할 정수들의 값들과 부호를 입력받아
# 연산의 결과를 반환하는 함수
# (정수들의 개수는 정해지지않음)
def calculator(*numbers, operator) :
    result = 0
    
    for num in numbers :
        if operator == "+" :
            result += num
        elif operator == "-" :
            result -= num
            
    return result

# 아래의 코드는 numbers 가변매개변수로 인해서
# '+' 문자까지 numbers 매개변수에 포함되어
# operator 매개변수의 값을 전달할 수 없습니다.
# (에러발생!)
#r1 = calculator(10, 20, '+')

# 가변매개변수 이후에 추가적인 매개변수가 존재하는 경우
# 반드시 명시적으로 매개변수의 이름과 함께
# 값을 전달해야만 에러가 발생하지 않습니다.
r2 = calculator(10, 20, operator='+')

print("Hello ", end="")
print("Python~!")
























