# 3초 / 정렬(계수정렬)
import sys
input = sys.stdin.readline

N = int(input())
count = [0] * 10001 # 주어진 숫자의 범위가 1~10000사이

for i in range(N):
    count[int(input())] += 1
    
for i in range(10001):
    if count[i] != 0:
        for _ in range(count[i]):
            print(i)
