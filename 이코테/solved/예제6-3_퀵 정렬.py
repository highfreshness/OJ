array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array, start, end):
    # 리스트에 원소가 하나만 있는 경우 종료
    if len(array) <= 1:
        return array

    pivot = array[0]  # 첫번째 원소
    tail = array[:1]  # 피벗을 제외한 원소

    left_side = [x for x in tail if x <= pivot]  # 분할된 왼쪽면
    right_side = [x for x in tail if x > pivot]  # 분할된 오른쪽면

    # 분할 후 왼쪽 오른쪽을 리스트에 원소가 하나만 있을 때 까지 재귀함수 형태로
    # 반복하고 최종적으로 정렬된 리스트를 합쳐서 리턴한다.
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


print(quick_sort(array))
