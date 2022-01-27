from itertools import cycle

answer = []
n, m, k = input().split()
arr = list(input().split())
arr.sort(reverse=True) # 내림차순 정렬
pattern = cycle( (arr[0] * int(k)) + arr[1] ) # 최대값 k번 반복 + 두번째 최대값 더하기 패턴 생성

# answer의 길이가 m보다 작을 때 까지 패턴을 반복하며 리스트 요소 추가
while len(answer) < int(m):
    answer.append(next(pattern)) 

# 최종 answer의 전체 합을 반환
print(sum(map(int, answer))) 



# # 문제 해답
# n, m, k = input().split()
# data = list(input().split())

# data.sort() # 오름차순 정렬
# first = data[n-1]
# second = data[n-2]

# count = int(m / (k + 1)) * k # 전체를 패턴의 길이로 나눈 뒤 k를 곱하면 최대값을 몇번 곱해야할지 알 수 있다.
# count += m % ( k + 1 ) # 위에서 나눈 뒤 남은 길이를 더해준다.

# result = 0
# result += count * first # 최대값을 count 만큼 더한다.
# result += ( m - count ) * second # 전체 길이에서 count를 뺀 만큼이 두번째 최대값에 곱해줄 수 이다.    
# print(result)