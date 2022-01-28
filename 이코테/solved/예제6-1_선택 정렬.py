# 오름차순 기준 정렬
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    # 가장 작은 숫자를 인덱스로 변환
    min_index = i
    for j in range(i + 1, len(array)):
        # 현재의 min_index가 j인덱스의 원소보다 크면 min_index의 값을 치환
        if array[min_index] > array[j]:
            min_index = j
    # i를 제외한 원소 중 최소값과 i를 스왑
    array[i], array[min_index] = array[min_index], array[i]

print(array)
