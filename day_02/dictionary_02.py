# -*- coding: utf-8 -*-

# 딕셔너리 내부에 저장된 데이터 추출 방법
# - 키 값을 활용
numbers = { "ONE" : 1, "TWO" : 2, "THREE" : 3 }

# [] 를 사용하여 값을 추출
print(f"ONE -> {numbers['ONE']}")
print(f"TWO -> {numbers['TWO']}")
print(f"THREE -> {numbers['THREE']}")

# [] 를 사용하여 값을 추출하는 경우
# 존재하지 않는 키값을 사용하면 에러가 발생됩니다.
print(f"FIVE -> {numbers['FIVE']}")

# 딕셔너리 변수의 get 메소드를 활용하여 값을 추출하는 경우
# 해당 키 값이 존재하면 저장된 Value 값이 반환되고
# 해당 키 값이 존재하지 않으면 None 값이 반환됩니다.
# None : 다른 프로그래밍 언어의 NULL 값과 같은 의미
#        아직 결정되지 않은 값을 의미
#        (존재하지 않는 값)
print(f"ONE -> {numbers.get('ONE')}")
print(f"TWO -> {numbers.get('TWO')}")
print(f"THREE -> {numbers.get('THREE')}")

# 아래는 FIVE 키 값이 존재하지 않기때문에
# None 값이 반환됩니다.
print(f"FIVE -> {numbers.get('FIVE')}")

















