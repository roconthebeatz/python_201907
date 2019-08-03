# -*- coding: utf-8 -*-

# 데이터베이스에 관련된 작업을 처리할 수 있는
# 클래스를 로딩
from DbController import DbController

# 클래스의 생성하여 데이터베이스 작업을 위한 준비
#controller = DbController("localhost", 3306, "root", "1234", "mydb")
controller = DbController("localhost", 3306)

sql = """
    select *
    from mytable
"""

# 쿼리의 수행 결과를 반환
result, result_count = controller.select(sql)

print("검색 개수 : ", result_count)

for record in result : 
    print(record)

# 클래스의 객체를 제거하여 데이터베이스 연결을 종료
del controller












