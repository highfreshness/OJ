"""
    1. 시간복잡도
        O(N)
    2. 변수
        N = 시험 과목의 수 
        scores = 시험 점수를 담은 리스트
        M = 최대 점수 값
"""

# 시험 과목 수를 입력받는다.
N = int(input())

# 시험 과목별 점수를 입력받는다.
scores = list(map(int, input().split()))

# 세준이의 시험 점수 조작 방식을 시험 과목별 점수에 대입한다.
M = max(scores)
scores = [(x / M ) * 100 for x in scores]

# 시험 점수의 평균을 출력한다.
print( sum(scores) / len(scores) ) 


