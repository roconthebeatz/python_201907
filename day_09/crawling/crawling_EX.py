# -*- coding: utf-8 -*-

# https://movie.naver.com/movie/sdb/rank/rmovie.nhn
# 으로부터 영화 랭킹 정보를 수집하세요
# 1 ~ 10위까지의 영화 제목을 추출하여 출력하세요.

import requests
from bs4 import BeautifulSoup as bs

url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'
session = requests.Session()
html = session.get(url).text

soup = bs(html, 'html.parser')
print(soup)

movies = soup.find_all(name='div',
                       attrs={'class':'tit3'},
                       limit=10)
print("COUNT : ", len(movies))

for i, movie in enumerate(movies) :
    #if i >= 10 :
    #    break
    print(f'{i+1} : {movie.a.text}')












