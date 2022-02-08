# 이진 탐색(재귀형태로 array[mid]==target이 될 때까지 반복)
def binary_search(array, target, start, end):
    # 시작점이 끝점보다 크면 None
    if start > end:
        return None

    # 중간점 = (시작점 + 끝점) / 2의 정수형태
    mid = (start + end) // 2

    # 중간점에 찾는 값이 존재한다면 인덱스 반환
    if array[mid] == target:
        return mid
    # 중간점의 값이 찾는 값보다 크면 end를 현재 중간점보다 한칸 앞의 인덱스로 변환하는 이진탐색을 다시 실행
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    # 중간점의 값이 찾는 값보다 작다면 중간점보다 하나 큰 인덱스를 시작값으로 이진탐색을 다시 실행
    else:
        return binary_search(array, target, mid+1, end)


n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    # 반환값이 인덱스 형태이기 때문에 +1을 해서 출력
    print(result + 1)
