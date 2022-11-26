import sys 
input = sys.stdin.readline

n, m = map(int, input().split())

numbers = list(map(int, input().split()))
prefix_sum = [0]
temp = 0

for x in numbers:
    temp += x
    prefix_sum.append(temp)
    
for _ in range(m):
    a, b = map(int, input().split())
    print(prefix_sum[b] - prefix_sum[a-1])