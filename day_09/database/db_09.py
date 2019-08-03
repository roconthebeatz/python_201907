# -*- coding: utf-8 -*-

from DbController import DbController

# 1. 수정할 아이디의 존재유무를 판단하여 아이디가 존재하는 경우
# 이름과 나이를 입력받을 수 있도록 제어
# (select 절의 실행 결과를 활용하여 아이디가 존재하는 경우만 2번으로 넘어감)
# 2. 이름 및 나이정보의 수정의사를 확인하여 처리할 수 있도록 제어
# EX) 이름을 수정하겠습니까?(y/n)

# 클래스의 생성하여 데이터베이스 작업을 위한 준비
controller = DbController("localhost", 3306, "root", "1234", "mydb")

my_id = int(input("수정할 아이디를 입력하세요 : "))
sql = f"""
    select *
    from mytable
    where id = {my_id}
"""
result = controller.select(sql)
if len(result) == 0 :
    print(f"입력한 아이디 {my_id}는 존재하지 않습니다.")
else :
    update_values = []
    
    isCheck = input("이름을 수정하겠습니까?(y/n)")
    if isCheck == 'y' or isCheck == 'Y' :
        update_value = input("수정할 이름을 입력하세요 : ")
        update_values.append(f"name = '{update_value}'")
        
    isCheck = input("나이를 수정하겠습니까?(y/n)")
    if isCheck == 'y' or isCheck == 'Y' :
        update_value = int(input("수정할 나이를 입력하세요 : "))
        update_values.append(f"age = {update_value}")

    update_str = None
    if len(update_values) > 1 :
        update_str = ",".join(update_values)
    else :
        update_str = update_values[0]
    
    sql = f"""
        update mytable
        set {update_str}
        where id = {my_id}
    """
    
    result_count = controller.update(sql)
    if result_count == 0 :
        print("수정작업이 완료되지 않았습니다.(아이디를 확인하세요)")
    else :
        print("수정 작업이 완료되었습니다.")
    
del controller










