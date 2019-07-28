# -*- coding: utf-8 -*-

# 사용자에게 5개의 성적을 입력받은 후,
# 각 성적의 그래프를 출력하세요.
# 성적의 최대값과, 최소값에 대해서 어노테이션을
# 추가하세요.
# (성적의 평균 점수를 나타내는 수평선을 추가)

index = list(range(1, 6))

# X 축의 데이터가 숫자로 지정되면 중간 단위의
# 값이 출력되므로 문자열로 변경처리
str_index = list(map(lambda x : str(x), index))

scores = []
for i in index :
    temp = float(input(f'{i}번째 성적 입력 : '))
    scores.append(temp)
    
max_score = max(scores)
min_score = min(scores)
avg_score = sum(scores) / len(scores)
max_index = 0
min_index = 0

for i in range(5) :
    if scores[i] == max_score :
        max_index = i
    if scores[i] == min_score :
        min_index = i
        
from matplotlib import pyplot as plt

plt.title('Scores')
plt.xlabel('Index')
plt.ylabel('Score')

plt.axhline(avg_score, color='g', linestyle='-.', linewidth=2)
plt.plot(str_index, scores)

plt.ylim(min_score - 5, max_score + 5)

plt.annotate('Max Score', 
             xy=(max_index, scores[max_index]),
             xytext=(max_index, scores[max_index]+7),
             arrowprops={'color': 'blue', 
                         'width' : 1})

plt.annotate('Min Score', 
             xy=(min_index, scores[min_index]),
             xytext=(min_index, scores[min_index]-7),
             arrowprops={'color': 'blue', 
                         'width' : 1})
    

plt.show()






















