# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
from random import random

x = list(range(1,11))
y = list(map(lambda data : data * random() + 3, x))

# 선의 타입을 변경하기 위한 방법
# plot 함수의 3번째 매개변수를 사용하여 변경
# - : 일반라인, -- : 대쉬라인, -. : 대쉬-닷라인 등등
# o : Circle Marker, v : 역삼각형, ^ : 삼각형
plt.plot(x, y, 'rv-.')

plt.show()