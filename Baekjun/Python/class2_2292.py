n = int(input())
temp = 1
cnt = 0

while(True):
    if temp < n :
        cnt += 1
        temp += cnt * 6
    else :
        print(cnt+1)
        break
