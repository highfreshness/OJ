array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

# array에 내부 숫자 범위만큼 빈 리스트 생성
cnt = [0] * (max(array) + 1)

# array의 숫자 요소를 하나씩 cnt에 카운트
for i in range(len(array)):
    cnt[array[i]] += 1

# cnt에 요소를 j번만큼 프린트해서 출력
for i in range(len(cnt)):
    for j in range(cnt[i]):
        print(i, end=" ")

