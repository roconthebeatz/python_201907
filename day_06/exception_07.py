# -*- coding: utf-8 -*-

# Calculator 클래스
# - +, -의 기능을 제공할 수 있는 클래스
# - 객체의 생성 시, 연산에 필요한 2개의
#   정수를 입력받을 수 있도록 구현됨
# - plus, minus 메소드의 호출시
#   연산의 결과를 화면에 출력

class Calculator :
    def __init__(self) : 
        # 연산에 필요한 두 정수를 저장하는
        # 인스턴스 변수의 선언
        self.n1 = None
        self.n2 = None
        # 연산의 결과를 저장하는 인스턴스 변수의 선언
        self.r = None
        
        # 인스턴스 변수에 값을 대입
        # - 숫자의 값만을 입력받을 수 있는
        #   메소드의 실행 결과를 대입
        self.n1 = self.inputNumber(1)
        self.n2 = self.inputNumber(2)
        
    def inputNumber(self, index) :
        n = None
        
        while True :
            try :
                n = int(input(f'{index}번째 숫자를 입력 : '))
            except :
                print("숫자 타입만 입력할 수 있습니다.")
                continue
            else:
                break
        
        return n

    def plus(self) :
        self.r = self.n1 + self.n2
        self.display('+')

    def minus(self) :
        self.r = self.n1 - self.n2
        self.display('-')
        
    def display(self, operator) : 
        print('{0} {1} {2} = {3}'.format(
                self.n1, operator, self.n2,
                self.r))

# 현재 파일이 실행 중인 상태라면
# 클래스를 테스트하는 아래의 코드가 실행
if __name__ == '__main__' :
    cal = Calculator()
    cal.plus()
    cal.minus()











