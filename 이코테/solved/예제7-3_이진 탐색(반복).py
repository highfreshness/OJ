# 이진 탐색(반복)
def binary_search(array, target, start, end):
    # 끝점이 시작점보다 크거나 같을 동안 반복
    while start <= end:
        # 중간점 설정
        mid = (start + end) // 2
        # 중간점의 값이 목표값이면 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점 값이 목표값보다 크다면 끝점을 중간점보다 1작은 인덱스로 대체한다.
        elif array[mid] > target:
            end = mid - 1
        # 중간점 값이 목표값보다 작다면 시작점을 중간점보다 1이 더 큰 인덱스로 대체한다.
        else:
            start = mid + 1
    # 반복문이 끝날 때 까지 리턴이 없는 경우 None을 반환한다.
    return None


n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    # 반환값이 인덱스 형태이기 때문에 +1을 해서 출력
    print(result + 1)
