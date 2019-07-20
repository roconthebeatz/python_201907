# -*- coding: utf-8 -*-

# 외부에서 import하여 사용할 함수의 정의
def printMessage(msg) :
    print(f'MESSAGE : {msg}')
    
# 모듈을 생성하는 경우 모듈 파일 내부의
# 실행문은 import 되는 시점에서도 실행됩니다.
# 만약 모듈 내부의 실행코드가 다른 파일에서
# import 되는 경우에 실행되지 않도록 제어하기 위해
# __main__ 네임스페이스를 사용합니다.
    
# 현재 파일이 실행중인 경우
# __name__의 값은 __main__ 이 됩니다.
print(f"__name__ -> {__name__}")

if __name__ == '__main__' :
    # 함수의 동작을 체크하는 테스트 코드
    printMessage("TEST MESSAGE")