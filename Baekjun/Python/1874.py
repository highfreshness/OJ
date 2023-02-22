# 2초 / 실버3 / 스택

# 수열 개수 입력
N = int(input())
A = [0] * N

for i in range(N):
    A[i] = int(input())

stack = []
num = 1 # 오름차순 자연수
result = True # 결과 분기용
answer = "" # 결과 모음

for i in range(N):
    su = A[i]
    if su >= num: # 오름차순 자연수보다 수열 값이 낮을 때
        while su >= num:
            stack.append(num)
            num += 1
            answer += "+\n"
        stack.pop() # 최종 수열 출력
    else: # 오름차순 자연수보다 수열 값이 높을 때
        n = stack.pop()
        if n > su: # 마지막 수열의 수가 현재 수열보다 크면 불가능(pop의 결과는 수열의 입력과 같아야 하기 때문)
            print("NO")
            result = False
        else:
            answer += "-\n"
if result:
    print(answer)
        