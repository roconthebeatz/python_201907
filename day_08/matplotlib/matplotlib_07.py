# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
from random import random

x1 = list(range(1,11))
y1 = list(map(lambda data : data * random() + 3, x1))

x2 = list(range(1,11))
y2 = list(map(lambda data : data * random() + 3, x1))

plt.title('Plot Example')

plt.xlabel('1 ~ 10')
plt.ylabel('random data')

# 여러 라인을 하나의 그래프에 출력할 수 있음

# 여러 라인을 하나의 그래프에 출력하는 경우
# 각 라인을 구분하기 위한 legend 출력 방법
# 1. plot 함수의 label 매개변수를 설정
# - 각 라인의 제목
plt.plot(x1, y1, '--r', label='First Data')
plt.plot(x2, y2, '--g', label='Second Data')

# 2. legend 함수의 loc 매개변수를 설정하여
# 어느 위치에 출력할 것인지 지정 
plt.legend(loc='best')

plt.show()










