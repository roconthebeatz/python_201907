# -*- coding: utf-8 -*-

# 문자열의 반복 처리
# - 문자열 데이터에 대해서 * 연산자를 사용
msg = "Hello Python~!"

# - 문자열 값에 대해서 * N 연산을 하는 경우
#  좌항의 문자열이 N번 반복된 결과가 반환
msg_multiply = msg * 10
print(msg_multiply)

# - 간단한 활용 예시
print("=" * 20)

# 문자열의 결합 연산
# 파이썬의 문자열은 + 연산자에 의해서
# '다른 문자열'과 결합될 수 있습니다.
part_1 = "Hello "
part_2 = "World~!"
merge = part_1 + part_2
print(merge)

# 문자열 결합의 잘못된 예시
# - 파이썬의 문자열 결합은
#   문자열 사이에서만 가능합니다.
n1 = 10
n2 = 5
msg = "10 + 5 = " + (n1 + n2)

# 만약, 문자열과 다른 타입의 값을 결합하려면
# str 함수를 사용할 수 있습니다.
# str 함수 : 다른 타입의 값을 문자열로 
# 변환하는 함수
# str(값)
msg = "10 + 5 = " + str(n1 + n2)
print(msg)



















