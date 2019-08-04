# -*- coding: utf-8 -*-

# 파이썬의 리스트는 + 연산의 경우 결합연산이 실행됨
python_list_1 = [1,2,3]
python_list_2 = [4,5,6]

python_list_sum = python_list_1 + python_list_2
print(python_list_sum)

import numpy as np

np_array_1 = np.arange(1,4)
np_array_2 = np.arange(4,7)

# numpy 배열의 경우 +, -, *, / 와 같은 연산을 수행하면
# 앞과 뒤의 배열에 대해서 각 위치에 해당되는 요소끼리
# 연산이 수행된 결과가 반환

np_array_r = np_array_1 + np_array_2
print(np_array_r)

np_array_r = np_array_1 - np_array_2
print(np_array_r)

np_array_r = np_array_1 * np_array_2
print(np_array_r)

np_array_r = np_array_1 / np_array_2
print(np_array_r)












