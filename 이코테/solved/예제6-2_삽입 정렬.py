# 선택 정렬과 비교해서 기존 array의 정렬도에 따라 속도가 달라진다 O(N) ~ O(N²)
# 오름차순 기준 정렬
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    # 현재 i에서 0까지 -1씩 감소하며 확인(왼쪽으로 비교)
    for j in range(i, 0, -1):
        # j가 j-1보다 작으면 서로 스왑
        if array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
        # j가 j-1보다 크면 j 반복문 종료
        else:
            break
print(array)
