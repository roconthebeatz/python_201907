# -*- coding: utf-8 -*-

# requests 모듈은 세션의 개념을 적용하여 
# 웹 데이터를 수신할 수 있는 모듈
import requests

# 통신 처리를 세션 객체를 생성
# 기존의 통신 정보를 유지하는 객체
# (세선 정보를 기록할 수 있는 객체)
session = requests.Session()

# 다운로드 대상의 주소값
url = 'http://img.hani.co.kr/imgdb/resize/2017/0804/00502237_20170804.JPG'

# 세션 객체를 사용하여 특정 요청을 실행하고, 
# 실행된 응답을 저장하는 코드
# response 변수는 응답에 관련된 데이터를 저장하고 있습니다.
response = session.get(url)

# response 변수의 status_code 의 값을 확인하여
# 현재의 요청이 올바르게 처리된 여부를 확인
# 200 -> 성공
# 400 -> 요청에러
# (URL 주소가 틀리거나, 전달해야하는 매개변수가 빠진경우)
# 500 -> 서버에러
# (서버측에서 데이터를 제공하기 위해 처리하는 중 에러가 발생)
print(response.status_code)

# 웹 리소스에 올바르게 접근했다면...
if response.status_code == 200 :
    fname = './download_01.jpg'
    with open(fname, 'wb') as f :
        # response 변수의 content를 파일에 기록하여
        # 파일에 저장
        # - content : 실제 웹 리소스의 데이터(이미지, 텍스트)
        f.write(response.content)













