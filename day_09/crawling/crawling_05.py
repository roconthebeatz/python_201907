# -*- coding: utf-8 -*-

# URL 정보를 활용하여 요청을 실행할 수 있는 모듈
import requests
from urllib.request import urlopen

url = 'https://finance.naver.com/'

# 세션 객체 생성
session = requests.Session()
# 세션 객체를 사용하여 웹 페이지에 접속
response_session = session.get(url)
# 응답 코드를 확인(200인 경우 성공)
print(response_session.status_code)
# 웹 페이지의 HTML 문서내용 확인
print(response_session.text)

# urlopen함수를 사용하여 웹 페이지의 접속
response_open = urlopen(url)
# 웹 페이지의 HTML 문서내용 확인
print(response_open.read())

from bs4 import BeautifulSoup as bs

soup = bs(response_session.text, 'html.parser')

#target = soup.find_all(name='div', 
#                       attrs={'class':'aside_popular'})
#print(len(target))

target_table = soup.select('div.aside_popular > table')
print(len(target_table))

items = target_table[0].select('th a')
print(len(items))

for i, item in enumerate(items) :
    item_name = item.text
    item_code = str(item.attrs['href']).split('?')[1]
    print(f'{i+1} : {item.text}({item_code})')


















