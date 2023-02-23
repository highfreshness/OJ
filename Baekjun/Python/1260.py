import sys
from collections import deque
sys.setrecursionlimit(10000)
input = sys.stdin.readline

# 초기 설정
n, m, s = map(int, input().split()) #노드, 엣지, 시작점
A = [[] for _ in range(n+1)] # 그래프 빈 노드 생성 
visited = [False] * (n+1) # 방문 체크

# 그래프 엣지 저장
for _ in range(m):
    start, end = map(int, input().split())
    A[start].append(end)
    A[end].append(start)
    
for i in range(1, n+1):
    A[i].sort() # 노드 정렬

def DFS(v):
    print(v, end=" ")
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            DFS(i)
            
DFS(s)
          
def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        now_node = queue.popleft()
        print(now_node, end=" ")
        for i in A[now_node]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
print()
visited = [False] * (n+1) # 방문 체크
BFS(s)



    


