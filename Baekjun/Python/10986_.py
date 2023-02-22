# 제한시간 1초, 합 배열
import sys

input = sys.stdin.readline
# n(수열의 개수), m(나눌 수) 입력
n, m = map(int, input().split())

# N개의 수 입력
list_a = list(map(int, input().split()))

# 선언 변수 초기화
sum_list = [0] * n
count_list = [0] * m
sum_list[0] = list_a[0]
answer = 0

# 합 배열 리스트 생성
for i in range(1, n):
    sum_list[i] = sum_list[i-1] + list_a[i]
    
for i in range(n):
    reminder = sum_list[i] % m # 합 배열 원소에 나머지 구하기
    if reminder == 0: # 연산 후 나머지가 0이면 정답 증가
        answer += 1
    count_list[reminder] += 1 # 결과 count
        
for i in range(m):
    if count_list[i] > 1:
        answer += (count_list[i] * (count_list[i]-1) // 2)
        
print(answer)
