# point : 시작칸과 마지막 칸(최우측하단)은 항상 1이다.
from collections import deque

# n, m 입력
n, m = map(int, input().split())
graph = []

# graph 입력
for x in range(n):
    graph.append(list(map(int, input())))

# 상하좌우 좌표    
dx = [-1, 1, 0, 0 ]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    # queue에 좌표 추가
    queue.append((x,y))
    # queue가 모두 비워질 때 까지 반복
    while(queue):
        # queue의 맨 첫번째 요소 추출
        x, y = queue.popleft()
        # 상하좌우 탐색 후 분기 처리
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # graph 공간을 넘어서는 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m;
                continue
            # 이동할 좌표가 0인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 이동할 좌표가 1인 경우 기존 좌표 값에 1 추가(누적)
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[nx][ny] + 1
                # 이동한 좌표를 queue에 추가
                queue.append((nx, ny))
    # 최우측 하단 방향(출구)까지 더해진 숫자 확인(최단거리)
    return graph[n-1][m-1]

print(bfs(0,0))
