# 1초 / deque / 골드 4
import sys
input = sys.stdin.readline

N = int(input())
answer = [0] * N
A = list(map(int, input().split()))
myStack = []

for i in range(N):
    while myStack and A[myStack[-1]] < A[i]:
        answer[myStack.pop()] = A[i]
    myStack.append(i)
    
while myStack:
    answer[myStack.pop()] = -1
    
result = ""

for i in range(N):
    result += str(answer[i]) + " "
    
print(result)
