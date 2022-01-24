d = int(input())
move = list(input().split())
point = [1, 1]

for x in move:
    if x == "U":
        if point[0] > 1:
            point[0] -= 1
        else:
            continue
    elif x == "D":
        if point[0] < d:
            point[0] += 1
        else:
            continue
    elif x == "R":
        if point[1] < d:
            point[1] += 1
        else:
            continue
    else:
        if point[1] > 1:
            point[1] -= 1
        else:
            continue

print(point[0], point[1])
