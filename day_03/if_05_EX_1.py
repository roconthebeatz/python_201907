# -*- coding: utf-8 -*-

# 3과목의 성적을 입력받아 총점과 평균
# 그리고 등급을 출력하세요
# 90점 이상 A, 80점 이상 B, 70점 이상 C,
# 60점 이상 D, 그 외에는 F

# 1. 입력
scores = input("3개의 성적을 입력(공백을 입력하세요) : ")
scores_split = scores.split()

score1 = int(scores_split[0])
score2 = int(scores_split[1])
score3 = int(scores_split[2])

# 2. 처리
total = score1 + score2 + score3
avg = total / len(scores_split)

grade = None
# 성적의 이상유무 확인
if avg > 100 or avg < 0 :
    grade = None
# 평균성적이 0 ~ 100 사이에 위치하므로
# 큰 값부터 시작하여 차례대로 비교
elif avg >= 90 :
    grade = 'A'
elif avg >= 80 :
    grade = 'B'
elif avg >= 70 :
    grade = 'C'
elif avg >= 60 :
    grade = 'D'
else :
    grade = 'F'

# 3. 출력
if grade == None :
    print("입력한 성적 점수에 문제가 발생했습니다.")
else:
    print(f"입력한 성적의 총점은 {total}점, 평균은 {avg:.2f} 입니다.")
    print(f"성적 평가는 '{grade}' 입니다.")










