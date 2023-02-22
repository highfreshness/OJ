# 투 포인터. 시간제한 : 2초
N = int(input()) # 자연수

sum = 1 # 순차적인 덧셈이 존재하지 않아도 자기 자신으로 1 확보
count = 1 # 순차적인 덧셈이 존재하지 않아도 자기 자신으로 1 확보
# 시작과 끝이 같은 위치에서 시작
start_point = 1 
end_point = 1

while end_point != N:
    if sum == N: # 순차로 더한 값이 N과 같을 때
        count += 1 # 정답 카운트 증가
        end_point += 1 # end_point 증가
        sum += end_point # end_point sum에 추가
    elif sum > N: # 모두 더한 값이 N보다 작은 경우
        sum -= start_point # sum에서 start_point만큼 차감
        start_point += 1 # start_point를 증가시켜 시작 위치 변경
    else:
        end_point += 1 # end_point 증가
        sum += end_point # sum에 end_point 추가

print(count)
