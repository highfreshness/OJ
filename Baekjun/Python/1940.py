# 2초, 투 포인트, 실버4
import sys
input = sys.stdin.readline

# n 입력
n = int(input())
# m 입력
m = int(input())
# 재료 입력
material = list(map(int, input().split()))
# 초기값 세팅
count = 0
i = 0
j = n-1
material.sort()
# 반복 i < j
while i < j:
    if material[i] + material[j] == m:
        count += 1
        i += 1
        j -= 1
    elif material[i] + material[j] < m:
        i += 1
    else:
        j -= 1
        
print(count)