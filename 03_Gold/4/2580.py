import sys
input = sys.stdin.readline

board = [list(map(int, input().strip().split())) for _ in range(9)]

c = [[False] * 10 for _ in range(10)]
c2 = [[False] * 10 for _ in range(10)]
c3 = [[False] * 10 for _ in range(10)]


def square(x, y):
    return 3 * (x // 3) + (y // 3)

for i in range(9):
    for j in range(9):
        if board[i][j] != 0:
            c[i][board[i][j]] = True
            c2[j][board[i][j]] = True
            c3[square(i, j)][board[i][j]] = True

def go(z):
    if z == 81:
        for i in range(9):
            print(*board[i], sep=' ')
        return
    x = z // 9
    y = z % 9
    if board[x][y] != 0:
        go(z + 1)
    else:
        for i in range(1, 10):
            if c[x][i] == False and c2[y][i] == False and c3[square(x, y)][i] == False:
                c[x][i] = True
                c2[y][i] = True
                c3[square(x, y)][i] = True
                board[x][y] = i
                go(z + 1)
                board[x][y] = 0
                c[x][i] = False
                c2[y][i] = False
                c3[square(x, y)][i] = False

go(0)