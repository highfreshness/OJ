n, m = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0
while (start <= end):
    total = 0
    mid = (start + end) // 2 
    for x in array:
        if mid < x :
            total += x - mid    
    if total < m :
        end = mid -1
    else :
        result = mid
        start = mid + 1
print(result)

# 시간 초과 답안
# cnt = max(array) - 1
# result = 0
# while result < m:
#     result = 0
#     for i in array:
#         if i > cnt :
#             result += i - cnt
#             cnt -= 1
#         else :
#             cnt -= 1
#             continue
# print(result)