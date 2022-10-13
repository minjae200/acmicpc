import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

r, c, k = map(int, input().split())
board = [ list(input()) for _ in range(r) ]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(y, x, move):
    global visited
    if y == 0 and x == c-1:
        if move == k:
            return 1
        else:
            return 0
    visited[y][x] = True
    ret = 0
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 > ny or ny >= r or 0 > nx or nx >= c:
            continue
        if board[ny][nx] == 'T' or visited[ny][nx]:
            continue
        ret += dfs(ny, nx, move+1)
    visited[y][x] = False
    return ret

visited = [[False] * c for _ in range(r)]
print(dfs(r-1, 0, 1))