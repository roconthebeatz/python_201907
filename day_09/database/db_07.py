# -*- coding: utf-8 -*-

from DbController import DbController

# 클래스의 생성하여 데이터베이스 작업을 위한 준비
controller = DbController("localhost", 3306, "root", "1234", "mydb")

sql = """
    select *
    from mytable
"""
result = controller.select(sql)

for record in result : 
    print(record)
    
del controller