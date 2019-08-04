# -*- coding: utf-8 -*-

import numpy as np

# 2행 2열의 이차원 배열 생성
np_array = np.array([[1,2],[3,4]])
print(np_array)

# numpy 배열의 모든 요소의 함계 값을 반환하는 
# sum 함수
result = np.sum(np_array)
print('np_array 배열의 전체 합계 : ', result)

# numpy 배열의 합계값은 각 행, 각 열에 대해서 
# 계산할 수 있습니다.
# axis = 0, 열
# axis = 1, 행
result = np.sum(np_array, axis=0)
print('np_array 배열의 각 열의 합계 : ', result)

result = np.sum(np_array, axis=1)
print('np_array 배열의 각 행의 합계 : ', result)

result = np.prod(np_array)
print('np_array 배열의 전체 곱셈의 결과 : ', result)

result = np.prod(np_array, axis=0)
print('np_array 배열의 각 열의 곱셈의 결과 : ', result)

result = np.prod(np_array, axis=1)
print('np_array 배열의 각 행의 곱셈의 결과 : ', result)
















