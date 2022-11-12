import sys

input = sys.stdin.readline

n = int(input())
num_list = list(map(int, input().split()))
point = {}
idx = 0

sort_num_list = sorted(num_list)


for x in sort_num_list:
    if x in point.keys():
        continue
    else:
        point[x] = idx
        idx += 1

idx = 0


for x in num_list:
    print(point[x], end=" ")
