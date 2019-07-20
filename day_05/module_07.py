# -*- coding: utf-8 -*-

# import 된 모듈 내부의 요소(변수, 함수, 클래스)에
# 접근하기 위해서는 모듈명을 사용해야 합니다.

# 만약, 모듈명 자체를 생략하고자 하는 경우
# from 모듈명 import 변수,함수,클래스명
# 으로 import 할 수 있습니다.

# from ~ import 절을 사용하여 요소를 가져오면
# 모듈명을 생략하고 변수,함수,클래스를 
# 사용할 수 있음

"""
from module_05 import num_05
print(num_05)

from module_05 import func_05
func_05()

from module_05 import Class_05
obj = Class_05()
"""

# from ~ import 를 사용하여 다수개의 요소를
# import 하는 예제
#from module_05 import num_05, func_05, Class_05
#print(num_05)
#func_05()
#obj = Class_05()

from module_05 import *
print(num_05)
func_05()
obj = Class_05()

# 파이썬의 기본 라이브러리를 import 하는 코드
# - import 키워드를 사용하여 불러올 수 있는 모듈은
#   현재 파일과 동일한 경로에 위치하거나
#   또는 시스템(운영체제)의 PATH 경로에 저장된
#   파일만 가능합니다.
import sys
import os
import csv


















