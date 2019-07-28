# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
from random import random

x = list(range(1,11))
y = list(map(lambda data : data * random() + 3, x))

plt.subplot(2,1,1)
plt.title('Plot Example')

plt.xlabel('1 ~ 10')
plt.ylabel('random data')

# BAR 형태의 차트 생성 방법
# bar, barh 함수를 사용
# bar(가로방향), barh(세로방향)
# bar(x데이터, y데이터)
# 참고사이트
# https://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.bar
plt.bar(x, y)

plt.subplot(2,1,2)
plt.title('Plot Example')

plt.xlabel('1 ~ 10')
plt.ylabel('random data')

# BAR 형태의 차트 생성 방법
# bar, barh 함수를 사용
# bar(가로방향), barh(세로방향)
# bar(x데이터, y데이터)
# 참고사이트
# https://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.bar
plt.barh(x, y)

plt.show()




