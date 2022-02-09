# 부품의 개수와 관계없이 재고 여부만 확인 하기 떄문에 집합 자료형을 이용해 풀 수 있다. 
n = int(input())
array = set(map(int, input().split()))

# 손님이 찾는 재고     
m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i in array:
        print('있음', ends=' ')
    else :
        print('없음', ends=' ')