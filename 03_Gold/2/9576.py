import sys
input = sys.stdin.readline

def dfs(x):
    for i in adj[x]:
        if visited[i]:
            continue
        visited[i] = True
        if occupy[i] == -1 or dfs(occupy[i]):
            occupy[i] = x
            return True
    return  False

for _ in range(int(input())):
    n, m = map(int, input().split())
    adj = [[] for _ in range(m)]
    for i in range(m):
        a, b = map(int, input().split())
        adj[i] = [ j for j in range(a, b+1)]
    matching = 0
    occupy = [-1] * (n+1)
    for i in range(m):
        visited = [False] * (n+1)
        if dfs(i):
            matching += 1
    print(matching)