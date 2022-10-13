import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n, m = map(int, input().split())
visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
board = [input().strip() for _ in range(n)]


redX, redY, blueX, blueY = -1, -1, -1, -1
for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            redX, redY = i, j
        elif board[i][j] == 'B':
            blueX, blueY = i, j

def _moveBall(x, y, direction):
    cx, cy = x, y
    move = 0
    while True:
        nx, ny = cx + dx[direction], cy + dy[direction]
        if board[nx][ny] != '#':
            move += 1
            cx, cy = nx, ny
            if board[nx][ny] == 'O':
                break
            continue
        break
    return cx, cy, move

def moveBall(redX, redY, blueX, blueY, direction):
    next_redX, next_redY, red_move_cnt = _moveBall(redX, redY, direction)
    next_blueX, next_blueY, blue_move_cnt = _moveBall(blueX, blueY, direction)

    if (next_redX, next_redY) == (next_blueX, next_blueY):
        if board[next_redX][next_redY] != 'O':
            if red_move_cnt < blue_move_cnt:
                next_blueX -= dx[direction]
                next_blueY -= dy[direction]
            else:
                next_redX -= dx[direction]
                next_redY -= dy[direction]

    return next_redX, next_redY, next_blueX, next_blueY

def bfs():
    visited[redX][redY][blueX][blueY] = True
    q = deque([(redX, redY, blueX, blueY, 0)])
    ret = -1
    while q:
        cur_redX, cur_redY, cur_blueX, cur_blueY, cnt = q.popleft()
        if cnt > 10: # 10 초과일 경우 종료 (-1)
            break

        # 성공 조건 (Red Ball만 빠졌을 경우)
        if board[cur_blueX][cur_blueY] != 'O' and board[cur_redX][cur_redY] == 'O':
            ret = cnt
            break

        # 위, 아래, 오른쪽, 왼쪽으로 기울였을 경우 체크
        for i in range(4):
            # 기울였을 때 공 위치
            next_redX, next_redY, next_blueX, next_blueY = moveBall(cur_redX, cur_redY, cur_blueX, cur_blueY, i)
            # 이미 방문한적이 있으면 무시
            if visited[next_redX][next_redY][next_blueX][next_blueY]:
                continue
            # Blue Ball이 빠졌을 경우 무시
            if board[next_blueX][next_blueY] == 'O':
                continue
            # 방문 처리
            visited[next_redX][next_redY][next_blueX][next_blueY] = True
            
            # 이 외의 경우라면 deque에 위치를 넣음
            q.append((next_redX, next_redY, next_blueX, next_blueY, cnt+1))
    return ret

print(bfs())