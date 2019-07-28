# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
from random import random

x = list(range(1,11))
y = list(map(lambda data : data * random() + 3, x))

# 그래프의 제목 설정
# title 함수를 사용
plt.title('Plot Example')

# 그래프의 라벨 설정
# xlabel, ylabel 함수를 사용
plt.xlabel('1 ~ 10')
plt.ylabel('random data')

plt.plot(x, y, '--r')

plt.show()