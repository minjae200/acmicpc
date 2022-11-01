n, m = map(int, input().split())
rect = [list(input().strip()) for _ in range(n)]

ans = 0
for i in range(n):
    for j in range(m):
        for k in range(min(n, m)):
            if (i + k) < n and (j + k) < m and (rect[i][j] == rect[i+k][j] == rect[i][j+k] == rect[i+k][j+k]):
                ans = max(ans, (k+1) ** 2)
print(ans)