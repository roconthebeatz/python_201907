# -*- coding: utf-8 -*-

from threading import Thread
# sleep 함수를 사용하기 위한 모듈 import
from time import sleep

class MyThread (Thread) :
    def run(self) :
        for i in range(1,11) :
            print(f"{self.getName()} -> {i}")
            # sleep 함수
            # 매개변수 전달된 정수에 해당되는 초만큼
            # 현재 쓰레드의 실행을 중지하는 기능을 제공
            # (실수도 가능)
            # 1 -> 1초, 0.5 -> 0.5초
            sleep(1)

t1 = MyThread(name="T1")
t2 = MyThread(name="T2")
t3 = MyThread(name="T3")

# 쓰레드 객체에 start 메소드를 호출하면 현재의 흐름에서 분기된
# 새로운 흐름이 생성되고 run 메소드가 실행합니다.(흐름의 분기 - 병렬실행)
t1.start()
t2.start()
t3.start()







