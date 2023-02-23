import sys
from queue import PriorityQueue

input = sys.stdin.readline
N = int(input())
count = 0

myQueue = PriorityQueue()
for i in range(N):
    myQueue.put(int(input()))

while myQueue.qsize() > 1:
    a = myQueue.get()
    b = myQueue.get()
    count += a + b
    myQueue.put(a + b)

print(count)
    