N = int(input())

board = [ list(input()) for _ in range(N) ]

dx = [1, 1, 0, -1, -1, -1, 0, 1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

ans = [ [0] * N for _ in range(N) ]

for x in range(N):
    for y in range(N):
        data = board[x][y]
        if data != '.':
            add = int(data)
            ans[x][y] = '*'
            for k in range(8):
                next_x = x + dx[k]
                next_y = y + dy[k]
                if 0 > next_x or next_x >= N or 0 > next_y or next_y >= N:
                    continue
                if ans[next_x][next_y] == '*':
                    continue
                ans[next_x][next_y] += add

for i in range(N):
    for j in range(N):
        print('M' if ans[i][j] != '*' and ans[i][j] >= 10 else ans[i][j], end='')
    print()