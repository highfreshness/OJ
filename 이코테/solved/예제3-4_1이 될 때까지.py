n, k = map(int, input().split())
result = 0

# while n != 1 :
#     if  n % k == 0:
#         n = n / k
#         result += 1

#     else :
#         n -= 1
#         result += 1

# n이 k보다 작은 경우 반복문 탈출

while True:
    target = (n // k) * k  # n을 k로 나눌 수 있는 가장 가까운 수
    result += n - target  # n에서 target을 빼 뺄셈해야할 수를 카운트
    n = target
    if n < k:
        break
    n //= k
    result += 1  # 한번 나누었기 때문에 나누기 1스택 추가

result += n - 1  # n이 k보다 작을 때 반복문을 나오기 때문에 1만 빼야 할 수 n 에서 -1을 해서 남은수가 1일 때를 고려함
print(result)
