# -*- coding: utf-8 -*-

from urllib.request import urlopen

url = 'https://www.newzealand.com/assets/Tourism-NZ/The-Coromandel/c827ae6373/img-1536337835-5322-19308-p-32099B6C-A0E5-CE51-BCD5CEA37CCF2767-2544003__FocalPointCropWzQyNyw2NDAsNTAsNTEsODUsImpwZyIsNjUsMi41XQ.jpg'

# URL 정보를 사용하여 웹 리소스에 접근하는 
# urlopen 함수의 사용법
# (단순연결 - 세션 X)
with urlopen(url) as response :
    # urlopen 함수는 매개변수로 입력된
    # URL로 접근하여 리소스의 정보를 추출할 수 있는 함수이며,
    # urlopen의 결과 변수에 대해서 read 메소드를 호출하여
    # 이미지 데이터를 추출
    content = response.read()
    
    fname = './download_02.jpg'
    with open(fname, 'wb') as f :
        # 이미지 데이터를 파일에 저장
        f.write(content)
    




















