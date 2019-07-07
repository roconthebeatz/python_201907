# -*- coding: utf-8 -*-

# dictionary_01.py

# Dictionary 데이터 타입
# - 다른 프로그램 언어의 MAP과 유사한 타입
# - 특정 데이터의 빠른 검색을 위해서 사용되는 데이터 타입
# - 데이터의 저장을 키와 밸류로 구성하여 저장
# - { KEY : VALUE }

program = { 'lang' : 'python', 'version' : 3.6 }
print(program)

# 딕셔너리의 데이터는 키와 밸류가 한 쌍이 됩니다.
# 위의 program 변수는 2개의 데이터를 가진 딕셔너리 변수
print(f"program's size -> {len(program)}")

# 딕셔너리 내부에 저장된 데이터 접근 방법
# - 키값을 사용하여 밸류에 접근
# - 딕셔너리변수[키값]
print(program['lang'])
print(program['version'])

# 딕셔너리 변수에 데이터를 추가하는 방법
# - 딕셔너리변수명[NEW KEY] = VALUE
program['level'] = 'high'
print(program)
print(f"program's size -> {len(program)}")





















