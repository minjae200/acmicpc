import sys
input = sys.stdin.readline

n, m = map(int, input().split())
occupy = [-1] * (n+1)
adj = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    adj[a-1].append(b)

def dfs(x):
    for i in adj[x]:
        if visited[i]:
            continue
        visited[i] = True
        if occupy[i] == -1 or dfs(occupy[i]):
            occupy[i] = x
            return True
    return False

matching = 0
for i in range(n):
    visited = [False] * (n+1)
    if dfs(i):
        matching += 1
print(matching)