# -*- coding: utf-8 -*-

# 클래스의 생성자
class Food :
    # 생성자의 선언
    # - 메소드
    # - __init__ 이름으로 고정된 메소드
    # - 생성자 메소드는 객체의 생성 시,
    #   자동으로 실행되는 메소드
    # - 생성자를 통하여, 각 객체의 인스턴스 
    #   변수의 생성을 처리할 수 있습니다.
    # - 생성자는 각각의 객체가 생성될 때마다
    #   실행되는 메소드    
    # - 생성자 매개변수의 기본값을 지정하여
    #   매개변수를 전달하지 않는 경우를
    #   처리할 수 있습니다.
    def __init__(self, name = None, price = None) :
        # 매개변수가 전달되지 않은 경우
        # 기본값으로 사용할 데이터를 처리하는
        # 분기문
        self.name = "간짜장" if name is None else name
        self.price = 7000 if price is None else price
    
    def setFoodInfo(self, name, price) :
        self.name = name
        self.price = price
        
    def printInfo(self) :
        print(f"{self.name}의 가격은 {self.price}원 입니다.")

# 일반적인 클래스의 객체 생성 과정
# 1. Food 클래스의 객체를 생성
f1 = Food()

# 인스턴스 변수가 생성되지 않았으므로, 에러가 발생
#f1.printInfo()

# 2. 인스턴스 변수 생성
f1.setFoodInfo("짜장면", 6000)
f1.printInfo()

# 생성자를 활용한 클래스의 객체 생성 과정
# 1. 클래스의 객체를 생성하기 위해서
#    생성자 메소드의 매개변수를 전달
# - __init__ 로 정의된 생성자 메소드는
#  객체를 생성할 때 클래스명() 으로 호출할 수 
#  있습니다.
# - 생성자에 의해서 인스턴스 변수가 객체의 생성
#   과정에서 자동으로 처리됨
f2 = Food('돈까스', 8000)
f2.printInfo()
















