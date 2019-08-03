# -*- coding: utf-8 -*-

import urllib.request

url = "http://image.chosun.com/sitedata/image/201804/23/2018042301907_0.jpg"

# 특정 URL로 요청을 수행하기 위한 Request 객체 생성
# 실제 요청이 실행되지 않음(정보만 저장하는 객체)
url_request = urllib.request.Request(url)
# 실제 요청을 수행하고, 요청의 결과값에 접근할 수 있는 변수 선언
url_connect = urllib.request.urlopen(url_request)
# 응답받은 데이터의 크기 값(바이트)
data_size = url_connect.length

# 한번에 수신할 데이터의 크기
buffer_size = 256
# 저장할 파일명
fileName = "./download_03.jpg"
with open(fileName, "wb") as f :
    # 다운로드 대상의 데이터를 버퍼의 크기만큼
    # 지속적으로 읽어들여 전체 데이터를 저장할 때까지
    # 반복을 수행
    while True :
        # 버퍼의 크기만큼 read 기능을 수행
        data = url_connect.read(buffer_size)
        # 데이터를 모두 읽어온 경우 반복을 중지
        if not data :
            break
        
        write_size = f.write(data)
        print(write_size)

url_connect.close()










