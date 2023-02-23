import sys
input = sys.stdin.readline

N, K = map(int, input().split()) # 동전 단위, 현재 금액
A = [int(input()) for _ in range(N)]
A.sort(reverse=True)
count = 0

for i in range(len(A)):
    if A[i] < K:
        count += K // A[i]   
        K = K % A[i]

print(count)