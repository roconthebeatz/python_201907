# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
from random import random

x = list(range(1,11))
y = list(map(lambda data : data * random() + 3, x))

plt.subplot(2,1,1)
plt.title('Plot Example')

plt.xlabel('1 ~ 10')
plt.ylabel('random data')

# color 속성은 색상 지정
# 기본값은 blue
plt.bar(x, y, color='red')

plt.subplot(2,1,2)
plt.title('Plot Example')

plt.xlabel('1 ~ 10')
plt.ylabel('random data')

# alpha 속성은 투명도 지정
# (0 ~ 1)
plt.barh(x, y, color='yellow', alpha=0.5)

plt.show()




