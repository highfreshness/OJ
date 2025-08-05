"""
    1. 풀이
        구간합
    2. 시간복잡도
        O( N  + M )
"""

import sys

input = sys.stdin.readline

# 2차원 배열의 크기, 질의 개수 입력
N, M = map(int, input().strip().split())

# 2차원 배열 입력
arr = [[0] * (N+1)]
for _ in range(N):
    arr.append([0] + list(map(int, input().strip().split())))  

# 구간합 배열 생성
sum_arr = [[0 for _ in range(N+1)] for _ in range(N+1)]
for x in range(1, N+1):
    for y in range(1, N+1):
        # 가로 구간합 + 세로 구간합 - 중복 구간합 + 배열의 값
        sum_arr[x][y] = sum_arr[x-1][y] + sum_arr[x][y-1] - sum_arr[x-1][y-1] + arr[x][y]  

# 질의 반복 수행
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().strip().split())
    print( sum_arr[x2][y2] - sum_arr[x1-1][y2] - sum_arr[x2][y1-1] + sum_arr[x1-1][y1-1] )
    