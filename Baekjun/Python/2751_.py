import sys
input = sys.stdin.readline
print = sys.stdout.write

def merge_sort(start, end): # start = 1, end = 5
    if end - start < 1: return # break의 효과
    mid = int(start + (end - start) / 2) # pivot 설정(=중간점)
    merge_sort(start, mid) # 첫번째 그룹 start - mid
    merge_sort(mid+1, end) # 두번째 그룹 mid+1 - end
    for i in range(start, end+1):
        tmp[i] = A[i]
        
    k = start
    index1 = start
    index2 = mid+1
    while index1 <= mid and index2 <= end:
        if tmp[index1] > tmp[index2]:
            A[k] = tmp[index2]
            k += 1
            index2 += 1
        else:
            A[k] = tmp[index1]
            k += 1
            index1 += 1
    while index1 <= mid:
        A[k] = tmp[index1]
        k += 1
        index1 +=1
    while index2 <= end:
        A[k] = tmp[index2]
        k += 1
        index2 += 1

N = int(input())
A = [0] * int(N+1) # index 1 ~ N까지
tmp = [0] * int(N+1)

for i in range(1, N+1): # A에 숫자를 입력 받음 index 1~N까지
    A[i] = int(input())

merge_sort(1, N) 

for i in range(1, N+1): # print를 실행하기 위함(str만 출력가능)
    print(str(A[i]) + "\n")