K, N = map(int, input().split())

cable = [int(input()) for _ in range(K)]

start, end = 1, max(cable)
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for x in cable:
        cnt += x // mid
    if cnt < N: 
        end = mid - 1
    else :
        start = mid + 1
print(end)
