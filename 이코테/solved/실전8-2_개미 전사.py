# 창고 수 n ( 3 <= n <= 100)
n = int(input())
# 식량 정보
array = list(map(int, input().split()))

# 계산 결과를 저장할 리스트
d = [0] * 100


d[0] = array[0]
d[1] = max[array[0], array[1]]
# i-1과 i-2를 비교했을 때 i-2는 한칸이 떨어져 현재 위치까지 더할 수 있음
for i in range(2,n):
    d[i] = max(d[i-1], d[i-2] + array[i])
    
print(d[n-1])