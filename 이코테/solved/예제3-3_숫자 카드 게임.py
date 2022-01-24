n , m = map(int, input().split())
arr = []
answer = 0

for x in range(n):
    arr.append(list(map(int, input().split())))
    
for i in arr:
    if answer < min(i):
        answer = min(i)
    
print(answer)