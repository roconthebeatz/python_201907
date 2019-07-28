# -*- coding: utf-8 -*-

"""
sales_2013.xlsx 파일의 데이터를 로딩하여
시각화 하세요.
x 축은 Customer Name, y축은 Amount 값을
사용하세요
"""

from matplotlib import pyplot as plt
import pandas as pd

input_fname = './data/sales_2013.xlsx'
sales = pd.read_excel(input_fname, 
                      sheet_name='january_2013',
                      index_col='Customer Name')

print(sales)

sales_amount = sales.iloc[:, 2]
sales_amount = sales.loc[:, 'Sale Amount']
print(sales_amount)

# pandas 데이타프레임 타입은 저장하고 있는 데이터를
# 시각화 할 수 있는 기능을 내장하고 있음
# 아래와 같이 plot 함수를 호출하면 인덱스는 X 데이터
# 각 데이터를 Y 데이터로 전달됩니다.
sales_amount.plot()

# 데이터프레임의 plot 함수를 호출한 이후에는 
# matplotlib 의 plt를 사용하여 각 설정이후
# 그래프를 출력할 수 있습니다.
plt.title('Sale Amount')
plt.xlabel('Name')
plt.ylabel('Amount')

"""
sales = pd.read_excel(input_fname, 
                      sheet_name='january_2013')

plt.title('Sale Amount')

plt.xlabel('Name')
plt.ylabel('Amount')

plt.plot(sales['Customer Name'], 
         sales['Sale Amount'],
         'go--')
plt.show()
"""




















