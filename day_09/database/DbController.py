# -*- coding: utf-8 -*-

import pymysql

# 데이터베이스에 관련된 작업을 처리할 수 있는
# 클래스의 선언
class DbController :
    # 생성자
    # 데이터베이스 커넥션 객체 생성
    def __init__(self, host, port, 
                 user='root', passwd='1234', db='mydb') :
        # 데이터베이스 커넥션 객체를 클래스의 멤버 변수로 저장
        self.db = pymysql.Connect(host=host,
                                  port=port,
                                  user=user,
                                  passwd=passwd,
                                  db=db)
        
    # 소멸자
    # 데이터베이스 연결 객체 종료 처리
    def __del__(self) :
        self.db.close()

    # 검색작업을 수행하는 메소드의 선언
    # 검색 결과 및 개수를 반환
    def select(self, sql) :
        result = None
        result_count = None
        
        with self.db.cursor() as cursor :
            cursor.execute(sql)
            result = cursor.fetchall()
            result_count = cursor.rowcount
            
        return result, result_count
            
    # 입력작업을 수행하는 메소드의 선언
    # - 가변 매개변수의 활용
    # - 크기(개수)가 고정되지 않은 매개변수
    def insert(self, table, *args):
        strArgs = ""
        
        #for i in range(len(args)):
        for i, value in enumerate(args) :
            if i > 0 :
                strArgs += ', '
            
            # 현재 추가할 데이터가 문자열이라면...
            # 앞뒤로 작은 따옴표를 추가
            if type(value) == type('') :
                strArgs += f"'{value}'"
            # 현재 추가할 데이터가 문자열이 아니라면
            # 작은 따옴표 없이 데이터만 추가
            else:
                strArgs += f"{value}"
            
        sql = f"""
            insert into {table}
            values ({strArgs})
        """
        
        # insert, update, delete 작업의 경우
        # execute 메소드의 실행 결과로
        # 적용된 레코드의 개수를 반환합니다.
        # - 만약 반환된 값이 0 이라면
        #  쿼리의 수행한 결과가 데이터베이스에
        #  영향이 없었다는 것을 의미함
        result_count = None
        with self.db.cursor() as cursor :
            result_count = cursor.execute(sql)
            self.db.commit()   
            
        return result_count

    def update(self, sql) :        
        result_count = None
        
        with self.db.cursor() as cursor :
            result_count = cursor.execute(sql)
            self.db.commit()
            
        return result_count
    
    def delete(self, sql) :        
        result_count = None
        
        with self.db.cursor() as cursor :
            result_count = cursor.execute(sql)
            self.db.commit()
            
        return result_count






















        