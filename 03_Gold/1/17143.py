import sys
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]
R, C, M = map(int, input().split())
sea = [ [None] * C for _ in range(R) ]
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    sea[r-1][c-1] = (s, d-1, z)


def getSeaAfterMove():
    global sea
    temp = [ [None] * C for _ in range(R) ]
    for i in range(R):
        for j in range(C):
            if not sea[i][j]:
                continue
            r, c, (s, d, z) = i, j, sea[i][j]
            loop = s
            while loop > 0:                    
                r += dr[d]
                c += dc[d]
                if 0 > r or r >= R or 0 > c or c >= C:
                    r -= dr[d]
                    c -= dc[d]
                    if d == 0: d = 1
                    elif d == 1: d = 0
                    elif d == 2: d = 3
                    elif d == 3: d = 2
                else:
                    loop -= 1
            if not temp[r][c]:
                temp[r][c] = (s, d, z)
            else:
                if temp[r][c][2] < z:
                    temp[r][c] = (s, d, z)
    return temp

ans = 0
for i in range(C):
    for j in range(R):
        if not sea[j][i]:
            continue
        ans += sea[j][i][2]
        sea[j][i] = None
        break
    sea = getSeaAfterMove()
print(ans)