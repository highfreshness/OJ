n = int(input())
num_list = list(map(int, input().split()))
cnt = 0

for x in num_list:
    if x == 1:
        continue
    else:
        for num in range(2, x + 1):  # 소수인지 판별하기 위한 반복문 1은 원래 포함되기 때문에 제외
            if (x % num) == 0:  # x % num의 나머지가 0이고 num이 라면 소수로 판단
                if num == x:
                    cnt += 1
                else:
                    break

print(cnt)
