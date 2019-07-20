# -*- coding: utf-8 -*-

# 부모클래스에 생성자 메소드가 정의된 경우의 사용방법

class Animal :
    def __init__(self, name, age, color) :
        self.name = name
        self.age = age
        self.color = color       
        
    def printInfo(self):
        print(f"name -> {self.name}")
        print(f"age -> {self.age}")
        print(f"color -> {self.color}")


class Dog (Animal) :
    pass

class Cat (Animal) :
    pass

# 부모클래스에 생성자가 정의된 경우
# 자식클래스는 부모클래스의 생성자를 상속받게 됩니다.
# 자식클래스의 객체를 생성할 때, 부모클래스의 생성자에
# 정의된 매개변수들을 전달해야만 객체를 생성할 수 있음
dog = Dog('강아지', 5, '갈색')
cat = Cat('고양이', 7, '흰색')

dog.printInfo()
cat.printInfo()


















