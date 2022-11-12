N, M = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()
start, end = 1, max(arr)

while start <= end:
    mid = (start + end) // 2

    cut_tree = 0
    for tree in arr:
        if tree > mid:
            cut_tree += tree - mid

    if cut_tree >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)
