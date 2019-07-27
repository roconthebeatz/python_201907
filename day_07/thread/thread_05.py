# -*- coding: utf-8 -*-

from threading import Thread
from time import sleep
from random import *

class RandomArrive (Thread) :
    def __init__(self, name) :
        # 부모 클래스의 생성자를 통한 이름 설정
        super().__init__(name=name)
    def run(self) :
        for _ in range(10) :
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

# 쓰레드 클래스의 join 메소드
# 해당 쓰레드의 실행이 종료될 때까지(run 메소드의 실행이 종료)
# 현재의 실행 흐름을 중지하는 기능을 제공
# 일반적으로 메인 흐름을 모든 쓰레드가 종료할 때까지 대기하는 역할
# (웹에서 데이터를 수집하는 쓰레드를 구동한 후, 데이터의 수집이
# 종료되면 메인 흐름을 동작시키는 등과 같이 활용)
for i in range(limit) :
    clients[i].join()

print("프로그램 종료")











