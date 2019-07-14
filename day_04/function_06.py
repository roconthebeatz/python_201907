# -*- coding: utf-8 -*-

# 개수가 정해지지 않은 매개변수를 처리하는 방법
# (가변매개변수)

# 입력된 매개변수들의 총 합계를 반환하는 함수
# (매개변수의 개수는 정해지지 않음...)
# 매개변수의 이름에 *를 사용하는 경우
# 가변매개변수로 처리되며, 개수가 고정되지 않음
# 이러한 경우 반복문을 사용하여 처리할 수 있음
def total(*numbers) :
    sumValue = 0
    for num in numbers :
        sumValue += num
    return sumValue

# 매개변수 numbers는 가변매개변수이므로
# 값이 전달되지 않아도 실행될 수 있음
total_0 = total()
print(total_0)

total_3 = total(10, 20, 30)
print(total_3)

total_5 = total(10, 20, 30, 40, 50)
print(total_5)






