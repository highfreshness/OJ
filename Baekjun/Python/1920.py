import sys

input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
A.sort()
M = int(input())
target_list = list(map(int, input().split()))

for i in range(M):
    find = False
    target = target_list[i] # 타겟 정의
    start = 0
    end = len(A)-1
    while start <= end:
        mid = ((start+end) // 2)
        mid_value = A[mid]
        if mid_value > target:
            end = mid_value - 1
        elif mid_value < target:
            start = mid_value + 1
        else:
            find = True
            break
    if find:
        print(1)
    else:
        print(0)
    