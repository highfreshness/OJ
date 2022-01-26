from collections import deque

# bfs 구현
def bfs(graph, start, visited):
    # deque 라이브러리를 이용해 queue 구현
    queue = deque([start])  # deque([1])
    # 시작 지점 방문 처리
    visited[start] = True
    # queue가 모두 빌 때 까지 반복
    while queue:
        # queue 요소 선입 선출 후 print
        v = queue.popleft()
        print(v, end=" ")
        # queue에서 뽑힌 원소의 연결 노드 정보를 추출
        for i in graph[v]:
            # 원소가 방문했던 위치가 아니라면 queue에 추가하고 방문 처리
            if not visited[i]:
                queue.append(i)
                visited[i] = True


graph = [
    [],  # 0번 노드 ( 존재 x )
    [2, 3, 8],  # 1번 노드와 연결된 노드 정보
    [1, 7],  # 2번 노드와 연결된 노드 정보
    [1, 4, 5],  # 3번 노드와 연결된 노드 정보
    [3, 5],  # 4번 노드와 연결된 노드 정보
    [3, 4],  # 5번 노드와 연결된 노드 정보
    [7],  # 6번 노드와 연결된 노드 정보
    [2, 6, 8],  # 7번 노드와 연결된 노드 정보
    [1, 7],  # 8번 노드와 연결된 노드 정보
]

# 방문 흔적을 남기기 위한 1차원 리스트 생성
visited = [False] * 9
bfs(graph, 1, visited)
