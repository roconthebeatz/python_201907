# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup as bs

# 운영체제에서 제공하는 기본적인 기능을 활용할 수 있는
# 함수를 제공하는 모듈
import os

try :
    if not os.path.isdir('./download'):
        os.makedirs(os.path.join('./download'))
except :
    print('Failed to create directory.')

url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'
session = requests.Session()
html = session.get(url).text

soup = bs(html, 'html.parser')
#print(soup)

movies = soup.find_all(name='div',
                       attrs={'class':'tit3'},
                       limit=10)
#print("COUNT : ", len(movies))

for i, movie in enumerate(movies) :    
    print(f'{i+1} : {movie.a.text}')
    
    # 링크 정보 추출을 위한 A태그 정보를 추출
    tag_a = movie.a
    # 이미지 파일의 이름을 지정하기 위한 텍스트 정보 추출
    movie_title = str(tag_a.text).replace(':', '_')        
    fname_image = os.path.join('./download/', movie_title + '.jpg')
    print('{0} : {1}'.format(i+1, fname_image))
    
    # 영화정보 페이지의 URL 정보를 저장하는 변수
    movie_info_page_url = 'https://movie.naver.com' + tag_a.attrs['href']
    #print('{0} : {1}'.format(i+1, movie_info_page_url))

    # 영화정보 페이지에 접근하여, HTML 내용을 추출한 후,
    # BeautifulSoup 객체를 생성
    movie_info_html = session.get(movie_info_page_url).text
    movie_info_soup = bs(movie_info_html, 'html.parser')

    movie_poster_tag = movie_info_soup.find_all(
            name='div', attrs={'class':'poster'})[1]
    #print(len(movie_poster_tag))
    #print(movie_poster_tag)

    movie_poster_img_tag = movie_poster_tag.img
    img_url = movie_poster_img_tag.attrs['src']
    print(img_url)
    
    # 이미지 파일 다운로드
    content = session.get(img_url).content
    with open(fname_image, 'wb') as f:
        f.write(content)
    












