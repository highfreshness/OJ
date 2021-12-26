cnt = int(input())
result = []

for x in range(cnt):
    a, b = map(int, input().split())
    result.append(a+b)
    
for prt in result:
    print(prt)