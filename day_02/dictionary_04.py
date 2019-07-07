# -*- coding: utf-8 -*-

# 딕셔너리 변수에 저장된 키의 값들을 반환받는 방법
# - keys 메소드를 사용

numbers = { "ONE" : 1, "TWO" : 2, "THREE" : 3 }

# 딕셔너리 변수의 keys 메소드는 현재 저장되어 있는 
# 모든 키 값을 반환
numbers_keys = numbers.keys()
print(numbers_keys)

# 딕셔너리 변수의 keys 메소드 결과를
# 리스트로 변환하는 방법
numbers_keys_list = list(numbers_keys)
print(numbers_keys_list)

# 반복문을 사용한 딕셔너리 내부의 데이터 순회방법
for key in numbers_keys_list :
    print("{0} : {1}".format(key, numbers[key]))

# 딕셔너리 내부에 저장된 모든 Value들을 반환하는 
# values 메소드    
numbers_values = numbers.values()
print(numbers_values)

# 딕셔너리 변수의 values 메소드 결과를
# 리스트로 변환하는 방법
numbers_values_list = list(numbers_values)
print(numbers_values_list)



















