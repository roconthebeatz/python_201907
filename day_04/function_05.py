# -*- coding: utf-8 -*-

# 파이썬의 함수/메소드는 하나가 아닌
# 다수개의 값을 반환할 수 있습니다.

# 두개 이상의 값을 반환하는 함수
# - 최대값과 최소값을 반환하는 함수
def max_and_min(n1, n2) :
    max_value = min_value = n1
    
    if n2 > max_value :
        max_value = n2
    
    if n2 < min_value :
        min_value = n2
    
    # 2개의 값을 반환하는 return 문
    # (다수개의 값을 반환하는 경우
    # 컬렉션 타입으로 반환되기 때문에
    # 1개의 변수로 반환값을 전달받을 수 있음)
    return max_value, min_value

# 컬렉션(튜플) 타입으로 리턴 값을 전달받는 경우
r = max_and_min(100, 200)
print(type(r))
print(r)
print(f"최대값 : {r[0]}, 최소값 : {r[1]}")

# 리턴되는 값을 각 변수에 대입받는 경우
r1, r2 = max_and_min(100, 200)
print(f"최대값 : {r1}, 최소값 : {r2}")

# 리턴되는 값의 개수보다 많은 변수에는
# 대입받을 수 없습니다.(에러발생)
#r1, r2, r3 = max_and_min(100, 200)

# 함수의 리턴값 중, 일부분의 값만을 사용하는 경우
# _ 선언 : 변수로 값을 전달받지 않고,
#         자리만 채우는 형식
r1, _ = max_and_min(100, 200)
_, r2 = max_and_min(100, 200)
_, _ = max_and_min(100, 200)













