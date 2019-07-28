# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
from random import random

x = list(range(1,11))
y = list(map(lambda data : data * random() + 3, x))

plt.title('Plot Example')

plt.xlabel('1 ~ 10')
plt.ylabel('random data')

plt.plot(x, y, '--r')

# 어노테이션 기능
# 그래프의 특정 데이터 위치에 대한 
# 설명문을 추가할 수 있는 기능
# annotate 함수를 통해 지정할 수 있음
# annotate(출력할문자열, 
# 타겟지점(xy), 
# 문자열출력지점(xytext), 
# 속성(arrowprops))
plt.annotate('5th Data', 
             xy=(x[4], y[4]),
             xytext=(x[4], y[4]+1),
             arrowprops={'color': 'blue', 
                         'width' : 1})

plt.show()












