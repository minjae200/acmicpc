import sys
input = sys.stdin.readline

n = int(input())
candy = [ list(input().strip()) for _ in range(n) ]

def count():
    cnt_x = 1
    for i in range(n):
        cnt = 1
        for j in range(n-1):
            if candy[i][j] == candy[i][j+1]:
                cnt += 1
            else:
                cnt = 1
            cnt_x = max(cnt_x, cnt)
    cnt_y = 1
    for j in range(n):
        cnt = 1
        for i in range(n-1):
            if candy[i][j] == candy[i+1][j]:
                cnt += 1
            else:
                cnt = 1
            cnt_y = max(cnt_y, cnt)
    return max(cnt_x, cnt_y)

def change(x, y, nx, ny):
    candy[x][y], candy[nx][ny] = candy[nx][ny], candy[x][y]

def check(x, y):
    cnt = 1
    if y+1 < n and candy[x][y] != candy[x][y+1]:
        change(x, y, x, y+1)
        cnt = max(cnt, count())
        change(x, y, x, y+1)

    if x+1 < n and candy[x][y] != candy[x+1][y]:
        change(x, y, x+1, y)
        cnt = max(cnt, count())
        candy[x][y], candy[x+1][y] = candy[x+1][y], candy[x][y]
    return cnt

ans = 0
for i in range(n):
    for j in range(n):
        ans = max(ans, check(i, j))
        if ans == n:
            print(ans)
            exit()
print(ans)