from re import M


n = int(input())
cnt = 0

hour = [h for h in range(n + 1)]
minute = [m for m in range(60)]
second = [s for s in range(60)]

for h in hour:
    for m in minute:
        for s in second:
            time = str(h) + str(m) + str(s)
            if time.find(str(n)) != -1:  # find 함수는 문자열에 n이 없다면 -1을 반환한다.
                cnt += 1

print(cnt)
