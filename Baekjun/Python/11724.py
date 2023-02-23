# 3초
import sys
sys.setrecursionlimit(10000) # 재귀 깊이 제한 설정
input = sys.stdin.readline

# 초기 설정
n, m = map(int, input().split()) # 노드, 엣지
A = [[] for _ in range(n+1)] # 그래프 인접 리스트 초기화
visited = [False] * (n+1) # 방문 체크 리스트

def DFS(v):
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            DFS(i)
            
for _ in range(m): # 엣지 개수만큼 실행
    start, end = map(int, input().split())  # 시작점, 끝점 입력
    # 방향이 없는 그래프로 시작점 끝점 모두 추가
    A[start].append(end)  
    A[end].append(start)
    
count = 0

for i in range(1, n+1):
    if not visited[i]:
        count += 1
        DFS(i)
        
print(count)