# -*- coding: utf-8 -*-

# 은행계좌 클래스의 선언
class Account :
    # 모든 Account 클래스의 객체들이 공유하는
    # 정보를 저장하기 위한 클래스 변수를 선언
    
    # 모든 계좌 객체들이 공유하는 은행이름 변수
    bank_name = "신한"
    # 모든 계좌 객체들이 공유하는 이자율 변수
    interest_rate = 0.03
    
    # 각각의 Account 객체들이 저장할 데이터를
    # 변수로 생성(인스턴스 변수)
    # - 공유의 개념이 아님
    def setAccountInfo(
            self, account_no, account_pw, balance) :
        self.account_no = account_no
        self.account_pw = account_pw
        self.balance = balance

    def interestProcess(self) :
        self.balance += self.balance * self.interest_rate
        
    def printBalance(self) :
        print(f"현재 잔액은 {self.balance} 원 입니다.")

# 2개의 계좌 객체 생성        
a1 = Account()
a2 = Account()

# 클래스 변수는 객체의 생성과 동시에
# 사용할 수 있는 변수
print(a1.bank_name)
print(a2.bank_name)
print(a1.interest_rate)
print(a2.interest_rate)

# 객체의 인스턴스 변수는 객체의 생성 이후,
# 인스턴스 변수를 생성하는 코드가 실행되어야만
# 사용할 수 있는 변수
# - 아래의 실행 코드는 아직 setAccountInfo 메소드가
#   실행되기 전이므로 AttributeError가 발생됨
print(a1.account_no)
print(a2.account_no)

# 각 객체들의 인스턴스 변수가 생성되는 시점
a1.setAccountInfo('1', 'ABC', 100000)
a2.setAccountInfo('2', 'def', 100000)

print(a1.account_no)
print(a2.account_no)

# 클래스 변수는 모든 객체들이 공유하는 정보로서
# 이자율과 같이 공통된 정보를 저장하기 위해서
# 사용됩니다.
print(a1.balance)
print(a2.balance)

# 모든 객체들이 공유하고 있는 interest_rate
# 클래스 변수의 값을 사용하여 이자를 지급
a1.interestProcess()
a2.interestProcess()

print(a1.balance)
print(a2.balance)

# 클래스 변수의 값을 수정하여
# 모든 객체들의 이자율을 일괄 수정하는 코드
Account.interest_rate = 0.5

a1.interestProcess()
a2.interestProcess()

print(a1.balance)
print(a2.balance)

# Account 클래스의 객체 생성 과정
# - 생성자가 존재하지 않는 경우의 실행코드 예제
# 1. 객체 생성
a3 = Account()
# 2. 인스턴스 변수 생성
a3.setAccountInfo('3', 'AAA', 10000)












