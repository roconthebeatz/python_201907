# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup as bs

html = '''
    <td class="title">
		<div class="tit3">
			<a href="/movie/bi/mi/basic.nhn?code=174903" title="엑시트">엑시트</a>
		</div>
	</td>
'''

soup = bs(html, 'html.parser')

# BeautifulSoup 객체의 find 메소드
# - 태그의 이름과 속성의 정보를 조합하여
# 검색하는 경우 활용
# - find 메소드는 검색 결과를 하나만 반환
# - 최초에 발견된 첫 번째 태그를 반환

# class의 속성이 title로 지정된 
# td 태그의 문서 정보 추출
tag_td = soup.find(name='td', 
                   attrs={'class':'title'})
print(tag_td)

# class의 속성이 tit3로 지정된 
# div 태그의 문서 정보 추출
tag_div = soup.find(name='div', 
                   attrs={'class':'tit3'})
print(tag_div)

# title의 속성이 엑시트로 지정된 
# a 태그의 문서 정보 추출
tag_a = soup.find(name='a', 
                   attrs={'title':'엑시트'})
print(tag_a)













