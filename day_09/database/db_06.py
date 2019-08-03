# -*- coding: utf-8 -*-

import pymysql

def getDBConnection(host, port, user, passwd, db) :
    conn = pymysql.Connect(host=host,
                           port=port,
                           user=user,
                           passwd=passwd,
                           db=db)
    return conn

#  데이터베이스 커넥션 객체 생성
db = getDBConnection("localhost", 3306, "root", "1234", "mydb")

# 데이터베이스에 쿼리를 실행할 수 있는 cursor 객체의 생성
# (자동 소멸을 지원하기 위해서 with 절을 사용)
with db.cursor() as cursor :   
    my_id = int(input("아이디를 입력하세요 : "))
    my_name = input("이름을 입력하세요 : ")
    my_age = int(input("나이를 입력하세요 : "))
    
    sql = f"""
        insert into mytable
        values ({my_id}, '{my_name}', {my_age});
    """
    try :
        cursor.execute(sql)
        db.commit()
    except Exception as msg :
        print(f"예외 발생 -> {msg}")
    else :
        print("입력 성공")

db.close()














