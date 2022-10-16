n, m = map(int, input().split())
cow = [[] for _ in range(n)]
answer = 0
occupy = [-1] * m

for i in range(n):
    a = list(map(int, input().split()))
    for j in a[1:]:
        cow[i].append(j-1)

def dfs(x):
    for i in cow[x]:
        if visited[i]:
            continue
        visited[i] = True
        if occupy[i] == -1 or dfs(occupy[i]):
            occupy[i] = x
            return True
    return False

for i in range(n):
    visited = [False] * m
    if dfs(i):
        answer += 1
print(answer)