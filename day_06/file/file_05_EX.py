# -*- coding: utf-8 -*-

# 성적 처리를 위해서 3과목의 성적을 입력받고
# 총점과, 평균을 계산하여 파일에 저장하세요 (scores.txt 파일)
# ex) 100,90,80,270,90.0

# 과목수
count = 3
# 과목의 성적을 저장하는 리스트 변수
scores = []
# 총점 저장 변수
tot = 0
# 평균 저장 변수
avg = None

for i in range(count) :
    # 사용자로부터 값을 입력받은 후, 리스트에 추가
    scores.append(int(input(f'{i+1}번째 성적 : ')))
    
    # 직전에 입력된 값을 총점에 누적
    #tot += scores[i]
    tot += scores[-1]

avg = tot / count

# 파일에 출력하기 위한 처리 작업

# 파일명 변수
output_file_name = 'data/scores.txt'

# a 모드 : append 모드
# (기존의 데이터를 삭제하지 않고 유지하는 모드)
output = open(output_file_name, 'a')

# 성적 정보를 복사하여 출력할 데이터의 리스트로 생성
output_data = scores.copy()
# 총점 정보를 출력할 데이터의 리스트로 추가
output_data.append(tot)
# 평균 정보를 출력할 데이터의 리스트로 추가
output_data.append(avg)

# CSV 포맷으로 데이터를 생성

# 문자열 결합의 규칙 때문에 아래의 코드는
# 에러가 발생
#output_data_str = ",".join(output_data)

output_data_str = ",".join(
        map(lambda x:str(x), output_data))

# 파일에 데이터 출력
output.write(output_data_str + '\n')

# 파일 객체 종료 및 버퍼에 있는 데이터를
# 파일로 출력
output.close()


























