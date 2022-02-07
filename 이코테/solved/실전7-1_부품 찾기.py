# store_parts = [8, 3, 7, 9, 2]
# m = int(input())
# search_parts = list(map(int, input().split()))

# for i in search_parts:
#     if i in store_parts:
#         print('Yes', end=' ')
#     else:
#         print('No', end=' ')

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end)//2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


n = int(input())
array = list(map(int, input().split()))
# 이진 탐색 전 정렬
array.sort()

m = int(input())
search_parts = list(map(int, input().split()))

for i in search_parts:
    result = binary_search(array, i, 0, n-1)
    if result == None:
        print('No', end=' ')
    else:
        print('Yes', end=' ')
