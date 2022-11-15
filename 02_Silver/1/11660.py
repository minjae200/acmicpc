import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = [ list(map(int, input().split())) for _ in range(n)]
partial = [[0] * (n + 1) for _ in range(n+1) ]

for i in range(1, n+1):
    for j in range(1, n+1):
        partial[i][j] = partial[i][j-1] + partial[i-1][j] - partial[i-1][j-1] + data[i-1][j-1]
    
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(partial[x2][y2] - partial[x1-1][y2] - partial[x2][y1-1] + partial[x1-1][y1-1])