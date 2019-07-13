# -*- coding: utf-8 -*-

# 사용자에게 3과목의 성적을 입력받아
# 평균점수가 90점이상이면 합격, 미만이면 
# 불합격을 출력하세요.

# 1. 입력 과정
score1 = score2 = score3 = None

#score1 = int(input('1번째 성적 입력 : '))
#score2 = int(input('2번째 성적 입력 : '))
#score3 = int(input('3번째 성적 입력 : '))

scores = input('3개의 성적을 입력(공백을 기준으로 입력하세요) : ')
# 문자열의 split함수는 공백을 기준으로 문자열을
# 분할하여 리스트로 반환합니다.
scores_split = scores.split()
score1 = int(scores_split[0])
score2 = int(scores_split[1])
score3 = int(scores_split[2])

# 처리과정
total = avg = output = None

total = score1 + score2 + score3
avg = total / len(scores_split)

# 합격 / 불합격 메세지
if avg >= 90 :
    output = "합격"
else :
    output = "불합격"

# 3. 출력
print(f"당신의 평균 성적은 {avg:.2f}점, '{output}' 입니다.")

















