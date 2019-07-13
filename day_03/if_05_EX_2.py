# -*- coding: utf-8 -*-

# 1 ~ 12 사이의 정수를 입력받아 
# 해당 월의 일수를 출력하세요
# EX) 1 -> 31, 2 -> 28, 3 -> 31 ...

# 1. 입력
month = int(input('1 ~ 12 사이의 정수를 입력 : '))

# 2. 처리
month_31 = [1,3,5,7,8,10,12]
month_30 = [4,6,9,11]
day = None

if month > 12 or month < 0 :
    # pass : 실행하지 않고 건너뛰는 명령
    pass
#elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12 :
elif month in month_31 :
    day = 31
elif month in month_30 :
    day = 30
else :
    day = 28
    
# 3. 출력
if day == None :
    print("1 ~ 12 사이의 정수만 입력하세요.")
else:
    print(f"{month}월은 {day}일 까지 있습니다.")
    















