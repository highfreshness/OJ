n, m = map(int, input().split())

ice_hole = []
# 얼음판 생김새 리스트
for _ in range(n):
    ice_hole.append(list(map(int, input())))


def dfs(x, y):
    # 범위를 벗어난 경우 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 위치에 방문하지 않았다면 방문처리
    if ice_hole[x][y] == 0:
        ice_hole[x][y] = 1
        # 상하좌우 위치 재귀형태로 확인
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False


result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)
