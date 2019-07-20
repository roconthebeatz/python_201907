# -*- coding: utf-8 -*-

# 소멸자 메소드
# - 클래스의 객체가 소멸될 때,
#   자동으로 호출되는 메소드
#   (생성자와 반대의 개념)

# 객체가 소멸되는 시점
# - del 키워드에 의해서 각 객체는 소멸될 수 있음
# - del 객체명(변수명)

# 소멸자 메소드의 정의 방법
# def __del__(self) :
#   객체가 소멸될 때 수행할 작업
#   (파일에 정보를 저장, DB 처리 ...)

class Food :    
    def __init__(self, name = None, price = None) :        
        self.name = "간짜장" if name is None else name
        self.price = 7000 if price is None else price
        
    def printInfo(self) :
        print(f"{self.name}의 가격은 {self.price}원 입니다.")
        
    def __del__(self) :
        print(f"{self.name} 음식을 다 먹었습니다.")
        
food = Food()
food.printInfo()

# food 객체의 소멸
del food

# 소멸된 객체는 사용할 수 없습니다.
#food.printInfo() 


# 소멸자 메소드가 호출되는 시점
# 1. 특정 객체 변수에 다른 객체가 대입되는 경우
# - 해당 변수가 저장하고 있던 기존의 객체는 소멸됨

food = Food("짜장면")
# 기존의 객체가 소멸되면서 새로운 객체가 food
# 변수에 대입되는 모습을 확인할 수 있음
food = Food("돈까스")

# 2. del을 사용하여 객체를 소멸하는 경우
food_1 = Food("짜장면")
food_2 = Food("치킨")
food_3 = Food("돈까스")

# 각 객체가 소멸되면서, 소멸자 메소드가
# 실행되는 모습을 확인할 수 있음
del food_1
del food_2
del food_3











