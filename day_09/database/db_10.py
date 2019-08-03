# -*- coding: utf-8 -*-

from DbController import DbController

# 클래스의 생성하여 데이터베이스 작업을 위한 준비
controller = DbController("localhost", 3306, "root", "1234", "mydb")

my_id = int(input("삭제할 아이디를 입력하세요 : "))

sql = f"""
    delete from mytable    
    where id = {my_id}
"""

result_count = controller.delete(sql)
if result_count == 0 :
    print("데이터 삭제에 실패했습니다.(아이디를 확인하세요)")
else :
    print("삭제 작업이 완료되었습니다.")
    
del controller










