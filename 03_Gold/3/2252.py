import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
result = deque()

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1
for i in range(1, n+1):
    if indegree[i] == 0:
        result.append(i)
while result:
    student = result.popleft()
    for i in graph[student]:
        indegree[i] -= 1
        if indegree[i] == 0:
            result.append(i)
    print(student, end=' ')
