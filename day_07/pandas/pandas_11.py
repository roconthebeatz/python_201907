# -*- coding: utf-8 -*-

import pandas as pd

# 데이터프레임의 병합
# - concat 함수의 사용
# - 단순 데이터 연결을 지원
# - 기본 연산은 데이터프레임을 상하로 결합

s1 = pd.Series([1,2], index=['A','B'])
print(s1)

s2 = pd.Series([3,4,5], index=['C','D','E'])
print(s2)

r = pd.concat([s1, s2])
print(r)

df1 = pd.DataFrame({
            'year' : [2017],
            'gdp' : [2.8]
        })
print(df1)

df2 = pd.DataFrame({
            'year' : [2018, 2019],
            'gdp' : [3.2, 3.5]
        })
print(df2)

r = pd.concat([df1, df2])
print(r)

# - ignore_index 매개변수
#   기존의 각각의 시리즈, 데이터프레임이 가지고 있는
#   인덱스의 값을 무시하고 새롭게 재생성된 인덱스를
#   가지도록 제어하는 매개변수
r = pd.concat([df1, df2], ignore_index=True)
print(r)













