from collections import deque

N = int(input())


mydeque = deque()
[mydeque.append(x) for x in range(1, N+1)]
print(mydeque)

while len(mydeque) > 1:
    mydeque.popleft()
    mydeque.append(mydeque.popleft())

print(mydeque.pop())
    
    




