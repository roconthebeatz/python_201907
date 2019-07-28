# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
from random import random

x = list(range(1,11))
y = list(map(lambda data : data * random() + 3, x))

plt.title('Plot Example')

plt.xlabel('1 ~ 10')
plt.ylabel('random data')

# 그래프의 구간 확대 및 축소 방법
# xlim, ylim 함수를 사용
# xlim(x축의 최소값, x축의 최대값)
# ylim(y축의 최소값, y축의 최대값)

plt.xlim(5, 8)
plt.ylim(5, 8)

plt.plot(x, y, '--r')

plt.show()