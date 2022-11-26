n = int(input())
point = list(map(int, input().split()))
sum = 0

max_point = max(point)

for x in point:
    sum += (x / max_point) * 100
    
print(sum/n)
