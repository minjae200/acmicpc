import math
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [ list(input().strip()) for _ in range(n) ]
ans = -1

for i in range(n):
    for j in range(m):
        for row_d in range(-n, n):
            for col_d in range(-m, m):
                num = ''
                y, x = i, j
                while 0 <= y < n and 0 <= x < m:
                    num += board[y][x]
                    if row_d == 0 and col_d == 0:
                        break
                    if int(math.sqrt(int(num))) ** 2 == int(num):
                        ans = max(ans, int(num))
                    y += row_d
                    x += col_d
print(ans)