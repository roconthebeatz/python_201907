# -*- coding: utf-8 -*-

import pandas as pd

input_fname = './data/sales_2013.xlsx'

sales = pd.read_excel(input_fname, 
                      sheet_name='january_2013',
                      index_col=None)
print(sales)

# pandas DataFrame의 loc 연산

# loc[ 행의 정보(시작인덱스:종료인덱스), 열의 헤더 이름 ]
# - 추출한 열의 정보가 하나인 경우
print(sales.loc[:, 'Sale Amount'])

# loc[ 행의 정보(시작인덱스:종료인덱스), [열의 헤더 이름 ...] ]
# - 추출한 열의 정보가 다수개인 경우 열의 이름 정보를 리스트로 전달
print(sales.loc[:, ['Customer Name', 'Sale Amount']])


















