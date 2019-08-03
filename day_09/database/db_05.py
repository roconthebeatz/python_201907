# -*- coding: utf-8 -*-

import pymysql

db = pymysql.Connect(host="localhost",
                port=3306,
                user="root",
                passwd="1234",
                db="mydb")

cursor = db.cursor()

my_id = int(input("아이디를 입력하세요 : "))
my_name = input("이름을 입력하세요 : ")
my_age = int(input("나이를 입력하세요 : "))

sql = f"""
    insert into mytable
    values ({my_id}, '{my_name}', {my_age});
"""

# 데이터베이스에 쿼리를 적용할 때, 다양한 이유로 인하여
# 예외가 발생할 가능성이 높습니다.(제약조건 등의 이유)
# 쿼리를 실행하는 코드의 경우 반드시 예외처리를 해야만
# 프로그램의 진행에 문제가 발생하지 않습니다.
try :
    cursor.execute(sql)
    db.commit()
except Exception as msg :
    print(f"예외 발생 -> {msg}")
else :
    print("입력 성공")

cursor.close()
db.close()















