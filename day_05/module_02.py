# -*- coding: utf-8 -*-

# 현재 파일 외부에 정의된 파이썬 파일의 
# 변수/함수/클래스 ... 등을 참조하는 방법
# - import 키워드를 사용
# - import 외부에 정의된 파이썬 파일명(확장자는 제외)
import module_01

# import 된 외부의 파이썬 파일(모듈)의 변수, 함수,
# 클래스는 모듈명을 활용하여 접근할 수 있습니다.
# 모듈명.변수명, 모듈명.함수(), 모듈명.클래스명
print(module_01.module_01_msg)

module_01.module_01_func()
