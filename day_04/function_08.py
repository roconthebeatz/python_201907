# -*- coding: utf-8 -*-

# 함수 매개변수의 기본값 설정

# def 함수명(매개변수명 = 기본값)
# - 기본값이 지정된 매개변수는 함수의 호출 시,
#   값을 전달하지 않아도 정상적으로 실행될 수 있음
#   (기본값을 사용하여 실행됨)

def calculator(n1, n2, operator='+') :
    result = n1
    
    if operator == '+' :
        result += n2
    elif operator == '-' :
        result -= n2
    elif operator == '*' :
        result *= n2
    elif operator == '/' :
        result /= n2
    elif operator == '%' :
        result %= n2
        
    return result

# operator 매개변수를 전달하지 않았으므로
# 기본값인 + 가 적용되어 실행
r = calculator(15, 10)
print(r)
r = calculator(15, 10, operator='-')
print(r)
r = calculator(15, 10, '*')
print(r)
r = calculator(15, 10, '/')
print(r)
r = calculator(15, 10, '%')
print(r)
        
        
        
        
        
        
        
        
        
        
        
        