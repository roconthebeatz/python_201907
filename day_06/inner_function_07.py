# -*- coding: utf-8 -*-

# zip 함수
# 매개변수로 전달된 컬렉션 변수들로부터 각각 데이터를 추출하여
# 튜플의 형태로 반환하는 함수

subjects = ["kor", "eng", "math"]
scores = [100, 90, 80]

combine = list(zip(subjects, scores))
print(combine)

for title, score in zip(subjects, scores) :
    print(f"{title} -> {score}")
    
    
    
    
    
    
    
    
    
    
    
    
    