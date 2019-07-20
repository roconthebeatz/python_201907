# -*- coding: utf-8 -*-

# 오버라이딩 문법
# - 자식클래스에서 부모클래스로부터 물려받은
#   멤버필드(변수)/메소드를 새롭게 재정의하는 문법
# - 생성자 메소드 / 일반 메소드를 자식클래스의
#   용도에 맞게 정의할 수 있는 문법

class Animal :
    def __init__(self, name, age, color) :
        self.name = name
        self.age = age
        self.color = color       
        
    def printInfo(self):
        print(f"name -> {self.name}")
        print(f"age -> {self.age}")
        print(f"color -> {self.color}")

# 소리를 낼 수 있는 강아지 클래스의 선언
class Dog (Animal) :
    # 생성자 오버라이딩 문법
    # Dog 클래스에서 Animal 클래스의 생성자를
    # 사용하지 않고, 자체적으로 정의된 생성자로
    # 대체하는 문법
    # - 소리정보를 추가적으로 받을 수 있는 생성자 선언
    def __init__(self, name, age, color, sound) :
        # 부모클래스 생성자를 자식클래스에서
        # 오버라이딩 하는 경우
        # 부모클래스의 생성자는 호출되지 않습니다.
        # (부모클래스에서 생성했던 
        # 인스턴스 변수가 생성되지 않음)
        
        # 자식클래스에서 부모클래스의 생성자를 
        # 사용하지 않고 새롭게 생성자를 정의하는 경우
        # 부모클래스의 생성자를 명시적으로 호출하여
        # 부모클래스의 인스턴스 변수들이 올바르게
        # 생성될 수 있도록 해야합니다.
        
        # 부모클래스의 멤버를 명시적으로 호출하는 방법
        # - super() 메소드 사용
        # - 자식 클래스의 내부에서 super() 메소드를
        #   호출하면, 부모클래스의 참조값이 반환됩니다.
        # - 부모클래스의 생성자를 호출
        # - super().__init__(부모클래스의 생성자 매개변수)
        # - 자식 클래스에서 오버라이딩 한
        #   부모클래스의 메소드를 호출
        super().__init__(name, age, color)
        self.sound = sound
    
    # 부모클래스의 printInfo 메소드를 새롭게 재정의하여
    # (오버라이딩) sound 정보를 출력할 수 있도록 
    # 메소드를 오버라이딩하는 예제
    def printInfo(self):        
        # 부모클래스에 정의된 printInfo 메소드 호출
        # super() 메소드를 사용하여 부모클래스의 
        # 오버라이딩된 메소드를 호출할 수 있습니다.
        super().printInfo()
        
        # Dog 클래스의 추가적인 작업 정의
        print(f"sound -> {self.sound}")

# 점프를 뛸 수 있는 Cat 클래스의 선언
class Cat (Animal) :
    def __init__(self, name, age, color, jump):
        super().__init__(name, age, color)
        self.jump = jump
        
    def printInfo(self):
        super().printInfo()
        print(f"{self.name}가 점프를 합니다.({self.jump}M)")

dog = Dog('강아지', 5, '갈색', '멍멍')
dog.printInfo()

cat = Cat('고양이', 7, '흰색', 5.3)
cat.printInfo()

















