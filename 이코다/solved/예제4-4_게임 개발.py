"""
게임 기초 설정
"""
n, m = map(int, input().split())
#  * m 형태의 0으로 된 행렬 리스트
d = [[0] * m for _ in range(n)]
# 캐릭터의 현재 좌표, 방향 입력받기
x, y, direction = map(int, input().split())
# 현재 캐릭터 좌표의 값을 1로 변경해 방문 처리
d[x][y] = 1

# 맵 정보 입력 받기
arr = []
for i in range(n):
    # 입력 받은 정보를 arr에 리스트 형태로 넣어 행렬처럼 추가
    arr.append(list(map(int, input().split())))

# 북, 동, 남, 서 이동 좌표 설정
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 방향을 반시계 90도로 돌려주는 함수 음수가 되면 3으로 원복 시켜준다.
def turn_left():
    # 바깥 direction 함수를 함수 내부에서 처리하기 위해 global 변수 설정
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


cnt = 1
turn_time = 0

"""
게임 시작
"""
while True:
    turn_left()  # 방향 회전
    # 동서남북에 맞는 이동 위치만큼 현재 좌표에서 이동
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 정면에 가보지 않은 좌표나 육지인 경우
    if d[nx][ny] == 0 and arr[nx][ny] == 0:
        d[nx][ny] = 1  # 방문 처리
        # 계산 위치를 현재 위치로 변경
        x = nx
        y = ny
        cnt += 1  # 이동 시 증가
        turn_time = 0  # 회전수 카운트
        continue
    else:
        turn_time += 1  # 회전수 증가

    # 동서남북을 모두 돌았는데도 앞으로 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        # 뒤가 육지인 경우
        if arr[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다인 경우 게임 종료
        else:
            break
        # 좌표가 제자리로 돌아온 경우 이동 카운트 0으로 변경
        turn_time = 0

print(cnt)

