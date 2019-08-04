# -*- coding: utf-8 -*-

import numpy as np

X_train = np.arange(1, 11)
# np.random.rand 함수 : 난수를 반환하는 함수
# - 난수 : 0 ~ 1 사이의 실수의 값을 의미
# - np.random.rand 함수는 무작위로 난수를 발생시켜 반환
y_train = np.arange(1, 11) * (1 + np.random.rand(10))

print(X_train)
print(y_train)

from matplotlib import pyplot as plt

plt.figure(figsize=(10,7))
plt.scatter(X_train, y_train)
plt.show()

plt.figure(figsize=(10,7))
plt.scatter(X_train, y_train)
plt.plot(X_train, X_train * 1.35, 'r--')
plt.show()

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train.reshape(-1, 1), y_train)

print(model.coef_)
print(model.intercept_)

plt.figure(figsize=(10,7))
plt.scatter(X_train, y_train)
plt.plot(X_train, X_train * 1.70421126 - 1.2543335647, 'r--')
plt.show()














