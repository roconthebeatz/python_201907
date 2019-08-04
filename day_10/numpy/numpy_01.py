# -*- coding: utf-8 -*-

"""
numpy 모듈
- numpy 모듈은 수치 계산을 위한 라이브러리
- 다차원 배열을 처리하는데 필요한 다양한 기능을 제공
- 머신러닝 및 딥러닝 라이브러리들은 내부적으로 
  numpy 배열을 사용하여 수치 계산을 수행함
"""

# 설치 명령
# pip install numpy

# numpy 모듈을 사용하기 위한 선언문(import)
import numpy as np

# numpy 배열의 생성 방법
# 파이썬의 리스트를 사용하여 생성할 수 있음
# np.array(파이썬 리스트 / 리스트 변수)

# 파이썬의 리스트 선언
python_list = [1,2,3,4,5]

# numpy 배열 선언
numpy_array_1 = np.array(python_list)

# TYPE 확인
print("python_list's type -> {0}".format(type(python_list)))
print("numpy_array_1's type -> {0}".format(type(numpy_array_1)))

print('python list : \n', python_list)
print('numpy array : \n', numpy_array_1)

# numpy 배열의 요소 출력
print(f'numpy_array_1 : {numpy_array_1}')
print(f'numpy_array_1[0] : {numpy_array_1[0]}')
print(f'numpy_array_1[-1] : {numpy_array_1[-1]}')
print(f'numpy_array_1[2:4] : {numpy_array_1[2:4]}')

# numpy 배열의 형태(shape) 출력
# - numpy 배열의 차원 정보
# - 튜플의 형태로 반환
# - 1차원 배열인 경우 : (1차원배열의크기, ) 
# - 2차원 배열인 경우 : (행의크기, 열의크기) 
print(f'numpy_array_1.shape : {numpy_array_1.shape}')

# numpy 배열의 크기를 확인하는 방법
# 1. len 함수를 사용하여 확인
print(f'len(numpy_array_1) -> {len(numpy_array_1)}')
# 2. shape의 반환값을 사용하는 방법
# - numpy_array_1.shape -> (5,)
# - numpy_array_1.shape[0] -> 5
print(f'numpy_array_1.shape -> {numpy_array_1.shape}')
print(f'numpy_array_1.shape[0] -> {numpy_array_1.shape[0]}')

# numpy 다차원 배열을 생성하는 방법
# 2행 3열의 다차원 배열을 생성하는 예제
numpy_array_2 = np.array([[1,2,3],[4,5,6]])
print("numpy_array_2's type -> {0}".format(type(numpy_array_2)))
print("numpy_array_2 -> {0}".format(numpy_array_2))

# numpy 다차원 배열의 각 요소에 접근하는 인덱스 연산
# 2차원 배열인 경우 2개의 인덱스가 사용
# 배열명[행의 인덱스, 열의 인덱스]
print(numpy_array_2[0, 1])

# numpy_array_2 에서 6의 값을 출력하세요.
print(numpy_array_2[1, 2])
print(numpy_array_2[-1, -1])

# 다차원 배열의 크기를 반환받는 방법
# 1. len 함수의 결과를 사용
# - 2차원 numpy 배열의 경우 행의 크기 값이 반환
print(f'len(numpy_array_2) -> {len(numpy_array_2)}')
print(f'len(numpy_array_2[0]) -> {len(numpy_array_2[0])}')

# 2. shape의 결과를 사용
print(f'numpy_array_2.shape -> {numpy_array_2.shape}')

# shape 속성의 결과에 대해서 인덱스의 값을 0으로 
# 지정하는 경우 행의 값이 반환
print(f'numpy_array_2.shape[0] -> {numpy_array_2.shape[0]}')

# shape 속성의 결과에 대해서 인덱스의 값을 1으로 
# 지정하는 경우 열의 값이 반환
print(f'numpy_array_2.shape[1] -> {numpy_array_2.shape[1]}')









