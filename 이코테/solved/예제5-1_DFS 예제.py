# dfs 알고리즘 구현
def dfs(graph, start, visited):
    # 처음 방문한 위치에 방문처리
    visited[start] = True
    print(start, end=" ")
    # 선택된 노드에 인접한 노드 탐색
    for i in graph[start]:
        # 만약 해당 노드에 방문한 적이 없다면 dfs를 재귀 형태로 수행
        # 수행 과정에서 모든 노드가 방문처리가 될 때 까지 dfs함수 수행
        if not visited[i]:
            dfs(graph, i, visited)


graph = [
    [],  # 0번 실제 없으나 인덱스 처리가 용이하도록 생성
    [2, 3, 8],  # 1번 노드와 인접한 노드
    [1, 7],  # 2번 노드와 인접한 노드
    [1, 4, 5],  # 3번 노드와 인접한 노드
    [3, 5],  # 4번 노드와 인접한 노드
    [3, 4],  # 5번 노드와 인접한 노드
    [7],  # 6번 노드와 인접한 노드
    [2, 6, 8],  # 7번 노드와 인접한 노드
    [1, 7],  # 8번 노드와 인접한 노드
]

# 노드 방문 정보를 담을 1차원 리스트 생성
visited = [False] * 9

# 1번부터 dfs 탐색 시작
dfs(graph, 1, visited)
