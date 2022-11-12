n = int(input()) # 자연수 N
result = 0 # 결과 


# 1부터 n까지 i와 i를 쪼개 더한 수를 더해 n과 일치하는지 확인(아래부터 순차적으로 올라가기 떄문에 처음 i와 check가 맞는 순간이 가장 작은 생성자)
for i in range(1, n): 
    eachSum = sum(map(int, str(i)))
    check = i + eachSum
    if check == n:
        result = i
        break
        
print(result)