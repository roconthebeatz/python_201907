# -*- coding: utf-8 -*-

import pandas as pd

input_fname = './data/sales_2013.xlsx'

sales_1 = pd.read_excel(input_fname, 
                      sheet_name='january_2013',
                      index_col=None)
print(sales_1)

sales_3 = pd.read_excel(input_fname, 
                      sheet_name='march_2013',
                      index_col=None)
print(sales_3)

# 데이터프레임의 병합
# - merge 함수의 사용
sales_1_3 = pd.merge(sales_1, sales_3)
print(sales_1_3)

# pandas의 옵션 수정
# - 출력할 최대 컬럼의 개수를 수정
pd.options.display.max_columns = 100

# - merge 함수는 기본적으로 동일한 컬럼의 이름을
# 기준으로 병합
# - 만약 동일한 이름의 컬럼이 다수개인 경우
# 모든 컬럼의 데이터가 동일해야만 병합이 이뤄짐
sales_1_3_on = pd.merge(sales_1, sales_3, 
                        on=['Customer ID', 'Customer Name'])
print(sales_1_3_on)





















