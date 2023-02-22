# 제한 시간 1초
# 시간 복잡도 : O(N) - 100
n = int(input())
m = input()
result = 0

for x in m:
    result += int(x) 
    
print(result)