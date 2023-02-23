# 수학적 이해 없이 풀지 못하는 문제
# (n)
# (k) 는 nCk로 풀 수 있으며 식을 풀어쓴다면 아래와 같다고 한다.
# factorial(n) / (factorial(k) - factorial(n-k))
import sys

input = sys.stdin.readline

def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num-1)

n, k = map(int, input().split())

print(int(factorial(n) / (factorial(k) * factorial(n-k))) ) # 정답이 int형

