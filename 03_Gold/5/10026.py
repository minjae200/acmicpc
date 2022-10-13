import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

N = int(input())
board = [list(input().strip()) for _ in range(N)]

def bfs(x, y, value):
    global visited
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    while q:
        current = q.popleft()
        cur_x = current[0]
        cur_y = current[1]
        for i in range(4):
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]
            if 0 > next_x or next_x >= N or 0 > next_y or next_y >= N:
                continue
            if visited[next_x][next_y] or board[next_x][next_y] != value:
                continue
            visited[next_x][next_y] = True
            q.append((next_x, next_y))

ans1, ans2 = 0, 0
visited = [[False] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visited[i][j]:
            continue
        bfs(i, j, board[i][j])
        ans1 += 1

for i in range(N):
    for j in range(N):
        if board[i][j] == 'R':
            board[i][j] = 'G'

visited = [[False] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visited[i][j]:
            continue
        bfs(i, j, board[i][j])
        ans2 += 1

print(ans1, ans2)