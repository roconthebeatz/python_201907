# -*- coding: utf-8 -*-

import numpy as np

# numpy 배열의 생성 함수
# numpy 모듈의 함수를 사용하여 배열을 생성할 수 있음

# 1. np.zeros(배열의형태) : 입력된 형태의 배열을
# 생성하면서 모든 요소의 값을 0으로 초기화
# - 아래의 코드는 3행 2열의 다차원 배열이 생성되고
#   모든 요소의 값은 0으로 채워짐
np_array_0 = np.zeros((3,2))
print(np_array_0)

# 2. np.ones(배열의형태) : 입력된 형태의 배열을
# 생성하면서 모든 요소의 값을 1으로 초기화
# - 아래의 코드는 2행 2열의 다차원 배열이 생성되고
#   모든 요소의 값은 1으로 채워짐
np_array_1 = np.ones((2,2))
print(np_array_1)

# 3-1. np.arange(종료값) : 0부터 종료값 -1 까지의 
# 값을 가지는 1차원 numpy 배열을 생성하여 반환함
np_array_2 = np.arange(10)
print(np_array_2)

# 3-2. np.arange(시작값, 종료값) : 시작값부터 종료값 -1 까지의 
# 값을 가지는 1차원 numpy 배열을 생성하여 반환함
np_array_3 = np.arange(5, 10)
print(np_array_3)

# 3-3. np.arange(시작값, 종료값, 증가치) : 
# 시작값부터 종료값 - 1 까지의 값을 가지는 배열이 생성됨
# (1씩 증가되는 것이 아닌 증가치만큼 값이 증가/감소됨)
np_array_3 = np.arange(1, 10, 0.5)
print(np_array_3)

# 4. np.full(배열의형태, 값) : 입력된 형태의 배열을
# 생성하면서 모든 요소의 값을 지정한 값으로 초기화
# - 아래의 코드는 3행 3열의 다차원 배열이 생성되고
#   모든 요소의 값은 5으로 채워짐
np_array_4 = np.full((3,3), 5)
print(np_array_4)

# 5. np.eye(배열의 행의크기) : 
# - 2차원 배열을 생성하는 함수
# - 지정된 행의 크기를 갖는 배열을 생성
# - 대각선 방향으로 1의 값은 갖는 배열 생성(대각행렬)
# - 아래의 코드는 5행 5열의 다차원 배열이 생성되고
#   대각선 방향으로 1의 값이 채워짐
np_array_5 = np.eye(5)
print(np_array_5)

# - np.eye 함수의 M 매개변수의 값은 열의 크기를 의미
np_array_5 = np.eye(5, M=3)
print(np_array_5)

# - np.eye 함수의 K 매개변수의 값은 대각행렬의
#   시작 열의 인덱스를 의미
np_array_5 = np.eye(5, k=1)
print(np_array_5)





















