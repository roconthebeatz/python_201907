# -*- coding: utf-8 -*-

# pie 차트
# 카테고리 별 값의 상대적인 비교를 위한 그래프 생성
# pie 함수를 사용하여 생성
# pie(데이터크기, 간격정보(explode), 
# 데이터라벨(labels), 각데이터색상(colors))
# 참고 사이트
# https://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.pie

# 데이터 크기
sizes = [15, 30, 45, 10]
# 데이터 출력 시 다른 데이터와의 간격
explode = [0.3, 0, 0, 0.1]
# 데이터 라벨
labels = ['A', 'B', 'C', 'D']
# 데이터를 출력할 색상
colors = ['yellow', 'gold', 'red', 'green']

from matplotlib import pyplot as plt

plt.title('Pie Chart Example')
plt.pie(sizes, explode=explode, labels=labels, colors=colors)
plt.show()



















