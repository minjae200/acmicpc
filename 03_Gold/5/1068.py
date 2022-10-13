import sys
input = sys.stdin.readline

n = int(input())
parent = list(map(int, input().split()))
delete = int(input())
leaf = 0

def dfs(delete, parent):
    parent[delete] = -2
    for i in range(len(parent)):
        if delete == parent[i]:
            dfs(i, parent)

dfs(delete, parent)
ans = 0
for i in range(n):
    if parent[i] != -2 and i not in parent:
        ans += 1
print(ans)