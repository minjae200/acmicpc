import sys

input = sys.stdin.readline


N, M = map(int, input().strip().split())
board = [ input().strip() for _ in range(N) ]

ball = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 'o':
            ball.append((i, j))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def check(x, y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return False
    return True

def travel(step, pos1, pos2):
    if step == 11:
        return -1

    live1 = check(pos1[0], pos1[1])
    live2 = check(pos2[0], pos2[1])
    if not live1 and not live2:
        return -1
    if not live1 or not live2:
        return step

    ans = 11
    for i in range(4):
        pos1_nx = pos1[0] + dx[i]
        pos1_ny = pos1[1] + dy[i]
        npos1 = (pos1_nx, pos1_ny)
        if (check(pos1_nx, pos1_ny) and board[pos1_nx][pos1_ny] == '#'):
            npos1 = pos1
        
        pos2_nx = pos2[0] + dx[i]
        pos2_ny = pos2[1] + dy[i]
        npos2 = (pos2_nx, pos2_ny)
        if (check(pos2_nx, pos2_ny) and board[pos2_nx][pos2_ny] == '#'): 
            npos2 = pos2

        result = travel(step+1, npos1, npos2)
        if result == -1:
            continue
        ans = min(ans, result)
    return ans if ans != 11 else -1

print(travel(0, ball[0], ball[1]))

