# -*- coding: utf-8 -*-

import pandas as pd

input_file_name = "data/scores.txt"

scores = pd.read_csv(input_file_name, header=None)

print(scores.info())
print(scores.describe())

for i in range(len(scores)) :
    
    print(f"1번째 성적 : {scores.iloc[i,0]} 점")
    print(f"2번째 성적 : {scores.iloc[i,1]} 점")
    print(f"3번째 성적 : {scores.iloc[i,2]} 점")
    
    print(f"총점 : {scores.iloc[i,3]} 점, ", end='')
    print(f"평균 : {scores.iloc[i,4]:.2f} 점")
    
    print("=" * 30)

