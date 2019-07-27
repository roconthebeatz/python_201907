# -*- coding: utf-8 -*-

import pandas as pd

fname = './data/sales_2013.xlsx'

# pandas 모듈을 활용한 엑셀 파일 로딩 처리
# pandas 모듈의 read_excel 함수
# read_excel(엑셀파일명, sheet_name="읽어올sheet이름")
sales = pd.read_excel(fname, sheet_name="january_2013")

# pandas 모듈은 읽어온 데이터를 DataFrame으로 저장합니다.
# (테이블의 구조를 가진 자료형인 경우)
# - 1차원 데이터인 경우 Series 타입으로 저장
# - 3차원 데이터인 경우 Panel 타입으로 저장

# 데이터의 개수 및 형태를 확인할 수 있는 info 메소드
# - 결측 데이터의 체크도 가능함
print(sales.info())

# 데이터의 간단한 통계 정보를 확인할 수 있는 describe 메소드
print(sales.describe())

# Pandas DataFrame 내부에 저장된 데이터를 읽어오는 방법
# - 컬럼의 이름을 사용하여 접근
print(sales['Customer ID'])
print(sales['Invoice Number'])
# - 다수개의 컬럼 정보를 가지고 오는 경우
# - DataFrame변수명[['컬럼명1', '컬럼명N']]
print(sales[['Customer ID', 'Customer Name']])
# - 특정인덱스의 위치 값을 추출하는 경우
# - 인덱스 연산을 사용
print(sales['Customer Name'][2])
# - 슬라이싱 연산을 사용하여 특정 인덱스 영역의 값을
#   추출할 수 있음
print(sales['Customer Name'][2:])
print(sales[['Customer ID', 'Invoice Number', 'Sale Amount']][1:4])

# pandas DataFrame의 저장 정보를 엑셀 파일로 출력
# 1. 출력할 파일명 정보를 변수로 저장
output_fname = './data/sales_2013_copy_1.xlsx'
# 2. 출력 객체를 생성
writer = pd.ExcelWriter(output_fname)
# 3. 출력 객체를 사용하여 엑셀 파일로
#    DataFrame에 저장된 정보를 저장
sales.to_excel(writer, 
               sheet_name='copy',
               index=True)
# 4. 출력 객체의 save 메소드를 통해서
# 실제 저장을 수행
writer.save()














