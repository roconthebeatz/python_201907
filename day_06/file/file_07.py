# -*- coding: utf-8 -*-

# with 절
# with 절은 자동 종료가 필요한 변수의 선언 시
# 사용할 수 있는 구문
# with 변수(변수의 생성코드) as 별칭 :
# with 절에 선언된 변수는 with 영역에서만
# 사용할 수 있고, with 구문이 종료되면
# 자동으로 close 메소드가 호출됩니다.

input_file_name = "data/scores.txt"
# 아래의 input_file 변수는 with 영역이 종료되면
# 자동으로 close 처리됩니다.
with open(input_file_name, "r") as input_file :
    scores = input_file.readlines()
    print(scores)
    
    for score in scores :
        data = score.strip().split(",")
    
        print(f"1번째 성적 : {int(data[0])} 점")
        print(f"2번째 성적 : {int(data[1])} 점")
        print(f"3번째 성적 : {int(data[2])} 점")        
        print(f"총점 : {int(data[3])} 점, ", end='')
        print(f"평균 : {float(data[4]):.2f} 점")        
        print("=" * 30)




















