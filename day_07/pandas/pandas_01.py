# -*- coding: utf-8 -*-

# 설치 : pip install pandas
# 아나콘다설치 : conda install pandas

# pandas 모듈
# 데이터 분석을 위해서 사용하는 모듈
# 파일 처리와 같은 작업을 손쉽게 
# 처리할 수 있도록 지원하는 모듈
# dataframe 개념을 적용하여 데이터를 테이블의 형태로
# 처리할 수 있도록 함(시각화 기능도 지원)

import pandas as pd

# CSV 파일을 로딩하는 예제
# 1. 파일의 경로를 저장하고 있는 변수의 선언
fname_csv = './data/scores.csv'
# 2. pandas 모듈의 read_csv 함수를 사용하여
#   파일을 로딩
scores_csv = pd.read_csv(fname_csv)

print(scores_csv)

# EXCEL 파일을 로딩하는 예제
# 추가적인 모듈의 설치가 필요!
# - 엑셀 파일 Read, Write 모듈 설치
# - pip install xlrd
# - pip install xlwt
# - pip install openpyxl
# - pip install xlrd xlwt openpyxl

# 1. 파일의 경로를 저장하고 있는 변수의 선언
fname_excel = './data/scores.xlsx'
# 2. pandas 모듈의 read_csv 함수를 사용하여
#   파일을 로딩
scores_excel = pd.read_excel(fname_excel)

print(scores_excel)























