# 2초, 투 포인트, 골드 4
import sys
input = sys.stdin.readline

# n(전체 수의 개수) 입력
n = int(input())

# A(수의 리스트) 입력
arr = list(map(int, input().split()))
arr.sort()

# 초기값 설정
count = 0

for x in range(n): 
    temp = arr[:x] + arr[x+1:]
    left, right = 0, len(temp)-1
    while left < right:
        sum = arr[left] + arr[right]
        if sum == arr[x]:
            count += 1
            break
        if sum < arr[x]: left += 1
        else : right -= 1

print(count)
