import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
q = deque()

for x in range(n):
    comm = input().split()

    if comm[0] == "push_front":
        q.insert(0, comm[1])

    elif comm[0] == "push_back":
        q.append(comm[1])

    elif comm[0] == "pop_front":
        if q:
            print(q.popleft())
        else:
            print(-1)

    elif comm[0] == "pop_back":
        if q:
            print(q.pop())
        else:
            print(-1)

    elif comm[0] == "size":
        print(len(q))

    elif comm[0] == "empty":
        if q:
            print(0)
        else:
            print(1)

    elif comm[0] == "front":
        if q:
            print(q[0])
        else:
            print(-1)

    elif comm[0] == "back":
        if q:
            print(q[-1])
        else:
            print(-1)
