# -*- coding: utf-8 -*-

# 딕셔너리 타입은 키 값의 중복을 허용하지 않습니다.
program = {"lang" : "python", "version" : 3.6 }
print(program)

# 딕셔너리 변수에 동일한 키값으로 값을 입력하는 경우
# 새로운 데이터가 추가되지 않고
# 동일한 키의 Value가 수정됩니다.
program["lang"] = "java"
print(program)
