# 2초
import sys
import math
sys.setrecursionlimit(10000)
input = sys.stdin.readline
N = int(input())

def isPrime(num): # 1과 자신만 나눌 수 있는 수
    for i in range(2, int(math.sqrt(num)+1)): # 나눌 수가 1보다는 커야하기 때문, 약수의 특성으로 연산을 반으로 줄일 수 있음 
        if num % i == 0:
            return False
    return True

def DFS(num):
    if len(str(num)) == N: # 자릿수
        print(num)
    else:
        for i in range(1, 10): # 1~9까지
            if i % 2 == 0: # 짝수는 2로 나누어지기 때문에 소수가 아님
                continue
            if isPrime((num * 10)+ i):
                DFS((num * 10) + i)

# 일의 자리 소수부터 증가 시작
DFS(2) 
DFS(3)
DFS(5)
DFS(7)
        
    