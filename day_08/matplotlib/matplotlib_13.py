# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
from random import random

x = list(range(1,11))
y = list(map(lambda data : data * random() + 3, x))

plt.title('Plot Example')

plt.xlabel('1 ~ 10')
plt.ylabel('random data')

# 서로 다른 형태의 그래프를 하나로 취합하여 출력할 수 있음
plt.bar(x, y, color='red')
plt.plot(x, y, '--ob')

plt.axhline(sum(y) / len(y))

plt.show()




