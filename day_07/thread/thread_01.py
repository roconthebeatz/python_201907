# -*- coding: utf-8 -*-

from time import sleep

# Thread (쓰레드)
# 프로그램
# - 컴퓨터를 제어하기 위한 명령어 집합
# 프로세스
# - 프로그램이 메모리에 적재되어 CPU를 선점하고 있는 상태
# 멀티태스킹
# - 컴퓨터의 유휴시간을 감소시키기 위해서 나온 개념
# - CPU의 실행 시간을 작은 단위로 분할하여 다수개의 프로세스가
#   번갈아가면서 CPU를 선점하는 방식
# 쓰레드
# - 프로세스 내부의 흐름을 분기할 수 있는 방법
# - 입출력 블럭킹과 같은 블럭 현상을 회피하여 병렬처리를 
#   진행할 수 있도록 합니다.

# 파이썬에서 쓰레드를 활용하는 방법

# 1.쓰레드 모듈을 import
from threading import Thread

# 2. Thread 클래스를 상속받는 자식 클래스를 생성
class MyThreadClass (Thread) :
    # 3. Thread 클래스의 run 메소드를 오버라이딩하여
    # 해당 쓰레드 클래스가 수행할 작업을 정의
    def run(self) :
        for i in range(1, 11) :            
            print(f'i -> {i}')
            sleep(3)
            
# 4. 쓰레드 클래스의 객체를 생성
t = MyThreadClass()

# 5. 생성된 쓰레드 클래스의 객체의 start 메소드를 호출하여
#    쓰레드를 실행
# - 생성된 쓰레드의 객체에 start 메소드를 호출하면
#   a. 현재의 흐름과 분기된 처리 흐름을 생성
#   b. 해당 쓰레드 객체의 run 메소드를 자동 호출
#   c. run 메소드의 실행 코드가 종료되면
#      쓰레드가 자동 소멸됩니다.
t.start()

a = int(input('1번째 정수 입력 : '))
b = int(input('2번째 정수 입력 : '))
r = a + b
print(f'{a} + {b} = {r}')























