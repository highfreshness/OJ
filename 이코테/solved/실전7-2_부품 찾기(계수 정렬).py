# 가게 재고 등록
n = int(input())
# 1000001개의 값이 0인 빈 리스트 생성
array = [0] * 1000001

# 입력이 들어온 인덱스는 재고가 있는 것으로 판단하고 내부 값을 1로 변경
for i in input().split():
    array[int(i)] = 1

# 손님이 찾는 재고     
m = int(input())
x = list(map(int, input().split()))

for i in x:
    if array[i] == 1:
        print('있음', ends=' ')
    else :
        print('없음', ends=' ')