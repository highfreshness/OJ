# 0.5초 (1초에 1,000만 연산)
import sys 
input = sys.stdin.readline

n, m = map(int, input().split())

temp = 0 
sum_list = [0] # 실제 값은 1번 index 부터 시작되도록 0을 하나 추가
list_a = list(map(int, input().split()))

for x in list_a:
    temp += x
    sum_list.append(temp)
    
for x in range(m):
    q1, q2 = map(int, input().split())
    print(sum_list[q2]- sum_list[q1-1])
