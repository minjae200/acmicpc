import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
adj = [[] for _ in range(n)]
for i in range(n):
    works = list(map(int, input().split()))[1:]
    adj[i] = works

occupy = [-1] * (m+1)
matching = 0
def dfs(x):
    for i in adj[x]:
        if visited[i]:
            continue
        visited[i] = True
        if occupy[i] == -1 or dfs(occupy[i]):
            occupy[i] = x
            return True
    return False

for i in range(n):
    visited = [False] * (m + 1)
    if dfs(i):
        matching += 1

extra = 0
for i in range(n):
    if extra >= k:
        break
    visited = [False] * (m+1)
    if dfs(i):
        extra += 1

print(matching + extra)