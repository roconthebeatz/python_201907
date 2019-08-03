# -*- coding: utf-8 -*-

import pymysql

class DbController :    
    def __init__(self, host, port, user, passwd, db) :
        # 생성자에서 데이터베이스 연결 객체 생성
        self.db = pymysql.Connect(host=host,
                           port=port,
                           user=user,
                           passwd=passwd,
                           db=db)    
        
    def __del__(self) :
        # 소멸자에서 데이터베이스 연결 객체 종료
        self.db.close()     
        
    def execute(self, sql, iscommit=False) :
        result = None
        result_count = 0
        
        with self.db.cursor() as cursor :
            try :
                cursor.execute(sql)  
                if iscommit :
                    self.db.commit()                
                result = cursor.fetchall()
                result_count = cursor.rowcount
            except Exception as msg :
                print(f"Error -> {msg}")
                result = None
                result_count = 0
            
        return result, result_count
    
    def select(self, sql) :
        result, result_count = self.execute(sql)
        return result
    
    def insert(self, table, *args) :        
        # 전달 매개변수들를 insert 절의 values 절로 변환
        strArgs = ""
        for i in range(len(args)) :
            if i > 0 :
                strArgs += ", "
                
            if type(args[i]) == type("") :
                strArgs += f"'{args[i]}'"
            else :
                strArgs += str(args[i])
    
        sql = f"""
        insert into {table}
        values ( {strArgs} )
        """
        
        result, result_count = self.execute(sql, iscommit=True)
        # insert 절의 경우 추가된 레코드의 개수가 반환되기
        # 때문에 1인 경우 입력이 성공
        return result_count
                
    def update(self, sql) :
        result, result_count = self.execute(sql, iscommit=True)
        # update 절의 경우 수정된 레코드의 개수가 반환되기
        # 때문에 0인 경우 수정이 실패
        return result_count
    
    def delete(self, sql) :
        result, result_count = self.execute(sql, iscommit=True)
        # delete 절의 경우 삭제된 레코드의 개수가 반환되기
        # 때문에 0인 경우 삭제가 실패
        return result_count
        
        
        
    
    
    
    
    
    
    
    
    
    
        
        
        
        
        
        
        
        