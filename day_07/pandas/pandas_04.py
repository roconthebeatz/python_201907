# -*- coding: utf-8 -*-

import pandas as pd

input_fname = './data/sales_2013.xlsx'

sales = pd.read_excel(input_fname, 
                      sheet_name='january_2013',
                      index_col='Customer ID')
print(sales)

print(type(sales['Customer Name']))
print(type(str(sales['Customer Name'])))
print(str(sales['Customer Name']))
print(list(str(sales['Customer Name'])))

# pandas Series 객체에 대해서 
# str 속석에 접근하면 해당 컬럼의 데이터를
# 문자열 메소드에 적용한 결과를 반환받을 수 있음
# - 이름의 첫 글자가 J로 시작하는 대상을 검색하는 코드
print( sales['Customer Name'].str.startswith('J'))
# - 이름을 모두 소문자로 변경한 후,
#   첫 글자가 j로 시작하는 대상을 검색하는 코드
print( sales['Customer Name'].str.lower().str.startswith('j'))

# - 이름의 마지막 글자가 z로 시작하는 대상을 검색하는 코드
print( sales['Customer Name'].str.endswith('z'))

# - 이름 사이의 공백을 제거한 값을 반홛하는 코드
print( sales['Customer Name'].str.replace(' ', ''))

# - 이름의 첫 글자가 J로 시작하는 대상을 검색하여 모든 컬럼의 
#   데이터를 출력하는 예제
# - DataFrame변수명[진리형의 값을 반환하는 조건식]
sales[ sales['Customer Name'].str.startswith('J') ]





















