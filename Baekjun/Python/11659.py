"""
    1. 풀이
        구간합 
    2. 시간복잡도
        O(N)
"""
import sys
input = sys.stdin.readline

# 데이터의 수(N), 질문 횟수(M) 입력
N, M = map(int, input().strip().split())

# 구간합을 구할 대상 배열 입력(numbers)
numbers = list(map(int, input().strip().split()))

# 구간합용 배열(sum_numbers) 생성
sum_number = [0] # 배열 순서를 1부터 하기 위해 사전 생성
temp = 0 
for number in numbers:
    temp += number
    sum_number.append(temp)

# 질문 횟수만큼 구간합 계산
for _ in range(M):
    i, j = map(int, input().strip().split())
    print(sum_number[j] - sum_number[i-1])