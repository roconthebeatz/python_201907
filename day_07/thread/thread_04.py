# -*- coding: utf-8 -*-

from threading import Thread
from time import sleep
# 파이썬에서 제공하는 난수에 관련된 모듈
# 난수 : 0 ~ 1 사이의 임의의 수
from random import *

class RandomArrive (Thread) :
    def __init__(self, name) :
        # 부모 클래스의 생성자를 통한 이름 설정
        super().__init__(name=name)
    def run(self) :
        for _ in range(10) :
            # random 모듈의 random 함수는 난수를 반환합니다.
            # (0~1 사이의 값 반환 - float)
            sleepTime = random() * 3
            sleep(sleepTime)
        
        print(f"{self.getName()} 도착~!")

clients = []
limit = int(input("참여자 수를 입력하세요 : "))

for i in range(limit) :
    clients.append(
            RandomArrive(
                    input(f"{i+1}번째 참여자 이름을 입력하세요 : ")))

for i in range(limit) :
    clients[i].start()















