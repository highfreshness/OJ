t = int(input())
temp = []

for x in range(t):
    k = int(input())
    n = int(input())
    floor = [[int(x) for x in range(1, 15)]]
    for f in range(k):
        for h in range(n):
            temp.append(sum(floor[f][:h+1]))
        floor.append(temp)
        temp = []    
    print(floor[k][n-1])
    floor = []