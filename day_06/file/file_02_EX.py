# -*- coding: utf-8 -*-

# 구구단의 내용을 data/file_02_gugudan.txt에
# 출력하세요.

# 출력할 파일의 경로를 포함한 이름을 변수에 저장
output_file_name = 'data/file_02_gugudan.txt'

# 파일에 출력할 수 있는 파일 객체를 open 함수를
# 사용하여 생성
output = open(output_file_name, 'w')

# 파이썬의 리스트 객체를 사용하여
# 파일에 라인별로 일괄 출력할 수 있습니다
output_data = []

# 반복문을 수행하면서 구구단의 출력 내용을
# 리스트 객체에 추가
# - \n은 사용하지 않음
for dan in range(2, 10) :    
    output_data.append(f'{dan}단을 출력')    
    for mul in range(1, 10) :        
        output_data.append(f'{dan} * {mul} = {dan*mul}')
    output_data.append('')
    
#output.writelines(output_data)
output.writelines(map(lambda x:x+'\n', output_data))

#for dan in range(2, 10) :    
#    output.write(f'{dan}단을 출력\n')    
#    for mul in range(1, 10) :        
#        output.write(f'{dan} * {mul} = {dan*mul}\n')
#    output.write('\n')
    
output.close()

























