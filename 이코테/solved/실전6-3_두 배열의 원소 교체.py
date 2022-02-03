# 리스트의 길이 n과 비교 반복 횟수 k 입력
n, k = map(int, input().split())

# a, b 리스트 입력
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# a는 오름차순 정렬, b는 내림차순 정렬로 정렬 진행
a.sort()
b.sort(reverse=True)

for i in range(k):
    # 교환하는 a의 원소가 b의 원소보다 작은 경우 각자 스왑
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else :
        break
    
print(sum(a))