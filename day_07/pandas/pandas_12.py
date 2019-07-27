# -*- coding: utf-8 -*-

import pandas as pd

df1 = pd.DataFrame({
            'ID' : [123, 456, 789],
            'NAME' : ['둘리', '도우너', '또치']
        }, index=[0,1,2])
print(df1)

df2 = pd.DataFrame({
            'ACCOUNT' : ['A', 'B', 'C'],
            'BALANCCE' : [25000, 77000, 130000]
        }, index=[0,2,3])
print(df2)

print(pd.concat([df1, df2]))

# 데이터프레임의 병합
# - concat 함수의 사용
# - 단순 데이터 연결을 지원
# - 수평으로 데이터를 연결하는 경우 
#   axis=1로 인수를 설정
print(pd.concat([df1, df2], axis=1))














