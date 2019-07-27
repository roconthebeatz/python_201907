# -*- coding: utf-8 -*-

import pandas as pd

input_fname = './data/sales_2013.xlsx'

sales = pd.read_excel(input_fname, 
                      sheet_name='january_2013',
                      index_col=None)
print(sales)

# pandas dataframe 의 iloc 연산

# dataframe변수명.iloc[행의정보(시작인덱스:종료인덱스)]
print(sales.iloc[2:4])

# dataframe변수명.iloc[행의정보, 열의 정보]
print(sales.iloc[2:4, 1:4])

# dataframe변수명.iloc[행의정보, 열의 정보]
# - 추출할 열의 데이터가 하나인 경우 정수값을 입력
print(sales.iloc[2:4, 1])

# dataframe변수명.iloc[행의정보, 열의 정보]
# - 추출할 열의 데이터가 연속된 인덱스가 아닌 경우
#   리스트의 형태로 열의 인덱스 정보를 입력
print(sales.iloc[2:4, [0,1,3]])

















