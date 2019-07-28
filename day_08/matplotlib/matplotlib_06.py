# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
from random import random

x = list(range(1,11))
y = list(map(lambda data : data * random() + 3, x))

plt.title('Plot Example')

plt.xlabel('1 ~ 10')
plt.ylabel('random data')

plt.xlim(min(x) - 1, max(x) + 1)
plt.ylim(min(y) - 1, max(y) + 1)

# 차트 내의 특정 y 위치에 수평선을 작성하는 방법
# axhline 메소드를 사용
y_mean = sum(y) / len(y)
# axhline(y축의값, 옵션 ... )
plt.axhline(y_mean, color='g', linestyle='-.', linewidth=2)

# 차트 내의 특정 x 위치에 수직선을 작성하는 방법
# axvline 메소드를 사용
x_mean = sum(x) / len(x)
# axvline(x축의값, 옵션 ... )
plt.axvline(x_mean, color='g', linestyle='-.', linewidth=2)

plt.plot(x, y, '--r')

plt.show()














