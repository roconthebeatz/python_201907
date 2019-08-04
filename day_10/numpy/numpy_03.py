# -*- coding: utf-8 -*-

import numpy as np

# numpy 배열 생성
# [1 2 3 4 5 6 7 8 9 10]
np_array_1 = np.arange(1, 11)

print(f"np_array_1's shape -> {np_array_1.shape}")
print(f"np_array_1 -> {np_array_1}")

# numpy 배열의 형태를 수정할 수 있는 reshape() 메소드
# numpy배열변수.reshape(변경할 배열의 shape)
np_array_2 = np_array_1.reshape(2, 5)
print(f"np_array_2's shape -> {np_array_2.shape}")
print(f"np_array_2 -> {np_array_2}")

# reshape() 메소드 사용시 주의사항
# - 원본 배열의 요소의 수는
#  변경할 형태의 shape의 요소 개수를 
#  만족해야합니다.
np_array_3 = np_array_1.reshape(3, 3)
print(f"np_array_3's shape -> {np_array_3.shape}")
print(f"np_array_3 -> {np_array_3}")

# -1 매개변수가 사용되는 경우 나머지 매개변수 값에의해서
# 자동으로 계산된 값이 적용됩니다.
# (아래의 예의 경우 열의 수를 2로 고정하여 행의 수는
#  5로 처리됩니다.)
np_array_4 = np_array_1.reshape(-1, 2)
print(f"np_array_4's shape -> {np_array_4.shape}")
print(f"np_array_4 -> {np_array_4}")

# 다차원 배열의 형태를 1차원 배열로 변경
np_array_5 = np_array_4.reshape(10)
print(f"np_array_5's shape -> {np_array_5.shape}")
print(f"np_array_5 -> {np_array_5}")

np_array_5 = np_array_4.reshape(-1)
print(f"np_array_5's shape -> {np_array_5.shape}")
print(f"np_array_5 -> {np_array_5}")
















