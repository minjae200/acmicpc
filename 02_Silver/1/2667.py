import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
_map = [ list(input().strip()) for _ in range(N) ]
visited = [[False] * N for _ in range(N)]

dx = [-1 ,1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    visited[x][y] = True
    q = deque([(x, y)])
    total = 0
    while q:
        cx, cy = q.popleft()
        total += 1
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 > nx or 0 > ny or nx >= N or ny >= N:
                continue
            if visited[nx][ny] or _map[nx][ny] != '1':
                continue
            visited[nx][ny] = True
            q.append((nx, ny))
    return total

ans = 0
result = []
for i in range(N):
    for j in range(N):
        if _map[i][j] == '1' and not visited[i][j]:
            result.append(bfs(i, j))
            ans += 1
print(ans)
result.sort()
for data in result:
    print(data)