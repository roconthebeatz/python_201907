# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
from random import random

x1 = list(range(1,11))
y1 = list(map(lambda data : data * random() + 3, x1))

x2 = list(range(1,11))
y2 = list(map(lambda data : data * random() + 3, x1))

# 그래프 이미지의 크기 조정
plt.figure(figsize=(15, 10))

plt.subplot(2,2,1)
plt.title('Plot Ex 1')
plt.xlabel('1 ~ 10')
plt.ylabel('Random Data')
plt.plot(x1, y1, '--or', label='First Data')
plt.legend(loc='best')

plt.subplot(224)
plt.title('Plot Ex 1')
plt.xlabel('1 ~ 10')
plt.ylabel('Random Data')
plt.plot(x2, y2, '--^b', label='Second Data')
plt.legend(loc='best')

plt.show()




















