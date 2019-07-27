# -*- coding: utf-8 -*-

import pandas as pd

input_fname = './data/sales_2013.xlsx'
# 인덱스로 사용할 열을 지정하여
# 엑셀파일을 로딩하는 내용
# - index_col 매개변수를 사용
sales = pd.read_excel(input_fname, 
                      sheet_name='january_2013',
                      index_col='Customer ID')
print(sales)

# DataFrame의 각 열은 pandas의 Series 타입이 됩니다.
# - 일차원 데이터 타입으로 인지됨
sales_name = sales['Customer Name']
print(type(sales_name))

# pandas의 Series 타입은 value_counts 메소드를 사용할 수
# 있으며, 메소드의 실행 결과는 중복을 제거한 
# 각 데이터의 개수가 반환됨
sales_date = sales['Purchase Date']
print(sales_date.value_counts())

# 조건식을 사용하여 데이터를 검색하는 예제
# - 검색할 날자 데이터의 리스트
dates = ['2013-01-01', '2013-01-11', '2013-01-31']
# DataFrame을 사용하여 조건식을 만족하는 데이터를 추출하는 방법
# - DataFrame변수명[출력할컬럼명][조건식]
# - 조건식은 True, False의 값이 반환되는 식
# - pandas의 Series 타입은 isin 메소드를 제공하며
#   각 열의 데이터가 매개변수로 전달된 리스트 내부에 존재하는 경우
#   True의 값이 반환됨
sales_condition1 = \
sales[['Customer Name', 'Sale Amount','Purchase Date']][
        sales['Purchase Date'].isin(dates)]
print(sales_condition1)

# Sale Amount 컬럼의 값이 평균 이상인 경우의 데이터만
# 추출하는 예쩨
sales_condition2 = sales[['Customer Name', 'Sale Amount']][
        sales['Sale Amount'] >= sales['Sale Amount'].mean()]
print(sales_condition2)





























