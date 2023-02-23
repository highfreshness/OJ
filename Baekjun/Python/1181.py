import sys
from queue import PriorityQueue

input = sys.stdin.readline

N = int(input())

A = [input().strip("\n") for _ in range(N)]
# print(f"List : {A}")
A = set(A)
# print(f"SET : {A}")
myPQ = PriorityQueue()

for x in A:
    myPQ.put((len(x), x))
    
for _ in range(myPQ.qsize()):
    print(myPQ.get()[1])


