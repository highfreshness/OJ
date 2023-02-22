# 파이썬 정렬 O(NlogN)
# n = int(input())

# t_list = [int(input()) for _ in range(n)]
# t_list.sort()
# [print(x, end="\n") for x in t_list]

# 버블 정렬 O(N**2)
N = int(input())

A = [int(input()) for _ in range(N)]

for i in range(N-1): # 루프 횟수
    for j in range(N-1-i): #실제 비교
        if A[j] > A[j+1]:
            A[j+1], A[j] = A[j], A[j+1] # 위치 스왑
            
[print(x, end="\n") for x in A]