# -*- coding: utf-8 -*-

import pandas as pd

# 머신러닝을 활용할 회귀분석
# 회귀분석 : 입력데이터(X)에 대한 정답데이터(y)가
# 연속된 수치데이터인 경우에 사용되는 분석 방법

# 머신러닝 알고리즘을 각 클래스로 제공하는
# 사이킷-런 라이브러리
# - 대다수의 머신러닝 알고리즘을 제공하는 라이브러리
# - 알고리즘 검증하기 위한 다양한 데이터 셋을 제공

# load_boston : Boston Housing Price 데이터
# - 회귀분석용 데이터 셋
from sklearn.datasets import load_boston

# 데이터 셋 로딩
boston = load_boston()

# 입력데이터(X)를 추출
X = pd.DataFrame(boston.data)

# 정답데이터(y)를 추출
y = pd.Series(boston.target)

# 데이터의 일부분 확인
# (시작 부분의 5개)
print(X.head())
print(y.head())

# 머신러닝을 위한 클래스의 import
# - 선형회귀를 구현하고 있는 LinearRegression
from sklearn.linear_model import LinearRegression

# 머신러닝을 위한 클래스의 객체를 생성
model = LinearRegression()

# 머신러닝 모델 객체를 학습
# - fit 메소드를 사용하여 학습을 진행
# - fit 메소드의 매개변수로 X와 y의 값을 전달
# - 아래의 fit 메소드는 선형모델을 기반으로 구현된
#   LinearRegression 클래스의 객체를 학습
# - 선형방정식 만족시킬 수 있는 기울기, 절편의 값을
#   검색하는 과정을 수행
# - y = X * W + b
model.fit(X.values, y.values)

# 머신러닝 모델을 사용하여 예측
# - predict 메소드를 사용함
predicted = model.predict(X.iloc[:5])

# 예측 값 확인
print('예측 : \n', predicted)
print('정답 : \n', y.iloc[:5].values)











