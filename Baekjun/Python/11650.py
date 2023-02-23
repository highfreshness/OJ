# 1초 
import sys

input = sys.stdin.readline

N = int(input()) # 좌표 갯수
A = [] # 좌표 저장용 리스트

for _ in range(N):
    x, y = map(int, input().split())
    A.append((x, y)) # 튜플로 x,y 저장
    
A.sort(key=lambda x:(x[0], x[1])) # 정렬 시 정렬 기준 설정

for i in range(N):
    print(A[i][0], A[i][1])