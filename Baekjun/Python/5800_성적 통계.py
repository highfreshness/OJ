n = int(input())
gap = []

for x in range(n):
    score_list = list(map(int, input().split()))
    del score_list[0]
    score_list.sort()
    for y in range(len(score_list)-1):
        gap.append(score_list[y+1] - score_list[y])
    print(f'Class {x+1}')
    print(f'Max {max(score_list)}, Min {min(score_list)}, Largest gap {max(gap)}')
    temp = []
    gap = []
    