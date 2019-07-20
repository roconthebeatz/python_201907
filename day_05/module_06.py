# -*- coding: utf-8 -*-

# 아래와 같이 외부의 파일을 import 하는 경우
# import된 파일명.접근할요소의이름 으로 사용합니다.

"""
# 파일명을 모듈명으로 쓰는 경우
# 파일명이 반복되어 소스 코드 작업이 힘듬
import module_05

print(module_05.num_05)

module_05.func_05()

obj = module_05.Class_05()
"""

# import되는 파일의 이름 대신 별칭을 사용하는 방법
# (모듈명을 간소화 하는 방법)
# import 모듈명 as 별칭
import module_05 as m5

print(m5.num_05)

m5.func_05()

obj = m5.Class_05()





















