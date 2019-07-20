# -*- coding: utf-8 -*-

# 다양한 클래스의 작성 시, 중복되는 정보가 
# 발생할 수 있습니다.
# 이러한 경우 일반적으로 코드를 복사하는 방식으로 구현함
# - 클래스의 수정 시, 동일한 분류의 클래스들을
#   같이 수정해야함
"""
class Dog :
    def __init__(self) :
        self.name = None
        self.age = None
        self.color = None        
        
class Cat :
    def __init__(self) :
        self.name = None
        self.age = None
        self.color = None        
"""

# 클래스의 상속
# - 클래스의 재활용을 위한 문법
# - 기존에 작성된 클래스의 내용을 
#   코드 복사 아닌 문법으로써 재활용할 수 있음
# - 상속을 사용하여 재활용하는 경우
#   부모클래스(상속을 해주는 클래스)의 변경이
#   자식클래스(상속을 받는 클래스)에 즉시 반영됩니다.

# 상속을 위한 과정
# 1. 현재 사용하고 있는 클래스들을 조사하여
#    공통된 속성(멤버필드, 메소드)를 파악
# 2. 부모클래스의 선언
# - 기존의 클래스들에서 중복되고 있는 멤버 필드, 메소드를
#   포함하고 있는 클래스
# 3. 부모클래스를 상속받아 중복되는 코드를 제거

# 상속을 활용한 강아지, 고양이 클래스의 선언
# 1. 부모클래스인 Animal 클래스의 선언
class Animal :
    def __init__(self) :
        self.name = None
        self.age = None
        self.color = None       
        
    def printInfo(self):
        print(f"name -> {self.name}")
        print(f"age -> {self.age}")
        print(f"color -> {self.color}")

# 2. 자식클래스의 선언
# - 상속관계를 구현하는 클래스의 선언 방법
# - class 자식클래스명 (부모클래스명) :
class Dog (Animal) :
    # pass 키워드는 구현 코드를 미루기 위해서
    # 사용되는 키워드
    pass
class Cat (Animal) :
    pass

# 부모클래스인 Animal 클래스에서 인스턴스 변수를 생성
dog = Dog()
cat = Cat()

# 부모클래스의 printInfo 메소드를 사용할 수 있음5
dog.printInfo()
cat.printInfo()

















