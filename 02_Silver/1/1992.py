import sys
input = sys.stdin.readline

N = int(input().strip())
board = [ list(input().strip()) for _ in range(N) ]

def solve(x, y, n):
    value = board[x][y]
    diff = False
    for i in range(x, x + n):
        for j in range(y, y + n):
            if value != board[i][j]:
                diff = True
                break
        if diff:
            break

    if diff:
        print('(', end='')
        n = n // 2
        solve(x, y, n)
        solve(x, y + n , n)
        solve(x + n , y, n)
        solve(x + n, y + n, n)
        print(')', end='')
    else:
        print(value, end='')

solve(0, 0, N)