# -*- coding: utf-8 -*-

# 실행의 결과를 반환할 수 있는 함수의 선언
# def 함수명([매개변수...]) :
#   return 함수를 호출한 지점으로 반환할 값

# 두개의 매개변수를 전달받아
# 합계를 반환하는 plus 함수의 선언
def plus(n1, n2) :
    # return 키워드
    # - 함수의 실행을 종료할 때 사용하는 키워드
    # - 함수의 실행을 종료하고, 우항의 값을
    #   함수를 호출한 지점으로 반환하는 기능
    return n1 + n2

plus_r = plus(100, 200)
print(f"plus_r -> {plus_r}")

# 함수의 반환값 응용
# 함수의 반환값을 다른 함수의 매개변수로
# 사용할 수 있습니다.
plus_r = plus(
        int(input('정수1 : ')), 
        int(input('정수2 : ')))
print(f"plus_r -> {plus_r}")



















