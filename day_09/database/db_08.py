# -*- coding: utf-8 -*-

from DbController import DbController

# 클래스의 생성하여 데이터베이스 작업을 위한 준비
controller = DbController("localhost", 3306, "root", "1234", "mydb")

my_id = int(input("아이디를 입력하세요 : "))
my_name = input("이름을 입력하세요 : ")
my_age = int(input("나이를 입력하세요 : "))

result_count = controller.insert("mytable", my_id, my_name, my_age)
print(result_count)
    
del controller