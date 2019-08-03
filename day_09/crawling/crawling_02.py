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

# 각 태그에 지정된 속성값의 접근
# attrs 속성
# 해당 태그에 지정된 속성값을 Dictionary 타입으로 반환
# BeautifulSoup변수.attrs -> {태그속성들...}
# BeautifulSoup변수.attrs["속성이름"] -> 속성값
tag_td = soup.td
print(tag_td)
print(tag_td.attrs)
print(tag_td.attrs['class'])
print(tag_td.attrs['class'][0])

tag_div = soup.div
print(tag_div)
print(tag_div.attrs)
print(tag_div.attrs['class'])
print(tag_div.attrs['class'][0])

tag_a = soup.a
print(tag_a)
print(tag_a.attrs)
print(tag_a.attrs['href'])
print(tag_a.attrs['title'])











