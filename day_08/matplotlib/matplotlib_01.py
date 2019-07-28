# -*- coding: utf-8 -*-

# matplotlib
# 파이썬에서 데이타를 차트나 플롯(Plot)을 
# 그려주는 라이브러리 패키지
# 범용적으로 가장 많이 사용되는 데이타 시각화
# (Data Visualization) 패키지

# 홈페이지
# https://matplotlib.org 

# 일반적인 matplotlib import 구문
from matplotlib import pyplot as plt
from random import random

x = list(range(1,11))
y = list(map(lambda data : data * random() + 3, x))

print(x)
print(y)

# plot 함수는 매개변수로 전달된 두 개의 리스트 타입을
# 사용하여 선을 그리는 함수
plt.plot(x, y)

# show 함수는 화면에 표시하는 함수 
plt.show()















