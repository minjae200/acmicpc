import sys
input = sys.stdin.readline
INF = int(1e9)
n = int(input())
dp = [[INF] * (1 << n) for _ in range(n)]
graph = [list(map(int, input().split())) for _ in range(n)]

def dfs(cur, visited):
    # base case
    if visited == (1 << n) - 1:
        if graph[cur][0] == 0:
            return INF
        else:
            return graph[cur][0]

    if dp[cur][visited] != INF or dp[cur][visited] == -1:
        return dp[cur][visited]
    
    for i in range(1, n):
        if graph[cur][i] == 0: # 가는길이 없다는 뜻
            continue
        if visited & (1 << i):
            continue
        cost = dfs(i, visited|(1<<i))
        if cost == -1:
            continue
        dp[cur][visited] = min(dp[cur][visited],  cost + graph[cur][i])
    if dp[cur][visited] == INF:
        dp[cur][visited] = -1
    return dp[cur][visited]
print(dfs(0, 1<<0))