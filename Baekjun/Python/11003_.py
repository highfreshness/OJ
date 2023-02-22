# 2.4초 / 플래티넘 / 슬라이딩 윈도우
from collections import deque

# N = 12, L = 3
# now = 1 5 2 3 6 2 3 7 3 5 2 6
N, L = map(int, input().split())
mydeque = deque()
now = list(map(int, input().split()))

for i in range(N):
    # deque는 [1] = index와 [0] = 값의 튜플로 이루어져 있음
    while mydeque and mydeque[-1][0] > now[i]: # deque의 끝 원소와 now 리스트 값과 비교
        mydeque.pop()
    mydeque.append((now[i], i))
    if mydeque[0][1] <= i - L:
        mydeque.popleft()
    print(mydeque[0][0], end=' ')

