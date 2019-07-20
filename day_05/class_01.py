# -*- coding: utf-8 -*-

# 클래스 : 사용자 정의 자료형
# - 프로그램에서 처리할 데이터를 정의하기 위한 문법
# - 클래스의 내부에는 변수(프로그램에서 처리할 데이터 - 멤버필드)
#   함수(프로그램에서 처리할 기능 - 멤버메소드)를 정의할 수 있음

# 클래스의 선언 방식
# class 클래스명 [(상속받을 부모클래스명)] :
#   클래스 내부에 저장할 변수...
#   클래스 내부에 저장할 함수(메소드)...

# 클래스 선언
class First :
    message = 'Hello Python Class~!'
    
# 클래스는 선언된 이후 변수로 생성되어야 
# 사용할 수 있습니다.
    
# 클래스의 변수 생성 방법
# 변수명 = 클래스명()
obj = First()

# 타입 체크
print(f"obj's type -> {type(obj)}")
    
# 클래스 내부에 선언된 멤버 필드(변수), 멤버 메소드는
# 접근연산자(.)을 사용하여 접근할 수 있습니다.
print(f"obj.message -> {obj.message}")

# 클래스를 정의하지 않고 사용하는 기존의 방법
# 학생에 대한 정보를 출력하는 함수
def printInfo(sid, name, age) :
    print(f"학번({sid}) 학생의 이름은 {name}, 나이는 {age} 입니다.")

# 학생에 대한 정보를 저장하는 각 변수를 생성
s1_id = "123"
s1_name = "ABC"
s1_age = "24"

printInfo(s1_id, s1_name, s1_age)


# 클래스를 사용하여 학생 정보를 출력하는 예제

# 학생 정보를 저장하는 클래스의 선언
class Student :
    s_id = None
    s_name = None
    s_age = None
    
    def __init__(self, s_id, s_name, s_age) :
        self.s_id = s_id
        self.s_name = s_name
        self.s_age = s_age
    
    def printInfo(self) :
        print(f"학번({self.s_id}) 학생의 이름은 {self.s_name}, 나이는 {self.s_age} 입니다.")

s1 = Student('456', 'DEF', 23)
s1.printInfo()












