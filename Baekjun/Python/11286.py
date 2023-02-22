import sys
from queue import PriorityQueue

print = sys.stdout.write # write는 str만 출력 가능
input = sys.stdin.readline

N = int(input())
my_pq = PriorityQueue() # 값 제거 시 가장 작은 값을 먼저 제거

for i in range(N):
    nb = int(input())
    if nb == 0:
        if my_pq.empty():
            print("0\n")
        else:
            temp = my_pq.get()
            print(str(temp[1])+"\n") #입력값이 (절대값, 값) 이기 떄문에 값을 print
    else:
        # PQueue input 예시 (1, -1) 
        my_pq.put((abs(nb), nb)) # 먼저 절대값으로 정렬, 절대값이 같으면 값으로 정렬
        