"""
코사라주 알고리즘
주어진 방향 그래프의 역방향 그래프와 스택을 사용하여 SCC를 구하는 알고리즘이다. 방향, 역방향 그래프가 동일한 SCC를 구성한다는 것을 이용한 방법이다.
① 주어지는 방향 그래프와 그 그래프의 역방향 그래프를 만든다.
② 정점을 담을 스택을 만들고 임의의 정점부터 DFS를 수행한다.
③ DFS가 끝나는 순서대로 스택에 삽입하고, 아직 방문하지 않은 정점에 대해 DFS를 수행한다.
④ 모든 정점이 스택에 담긴 후에는 스택을 pop하여 나오는 정점부터 역방향 그래프에서 DFS를 수행한다.. 이미 방문한 정점은 pop만 시행한다.
⑤ 이때 탐색되는 모든 정점을 SCC로 묶는다.
이것을 스택이 빌 때까지 진행한다.
(타잔 알고리즘에 비해 구현이 더 쉬운 편이라고 한다.)

타잔 알고리즘
모든 정점에 대해 DFS를 수행하여 SCC를 찾는 알고리즘으로, 코사라주 알고리즘에 비해 적용이 더 쉽다고 한다.
① 인접 정점에 방문하며 자기 자신을 스택에 넣고, 재귀적으로 DFS를 수행한다.
② 인접 정점에 방문했지만, 아직 처리중인 상태일 경우, 작은 값으로 부모값을 갱신한다.
③ 부모 노드의 DFS가 끝난 경우에는, 자신의 id값이 스택에서 나올 때까지 스택에 있는 노드들을 pop하고 scc 배열에 추가한다.
④ 만들어진 하나의 scc를 전체 SCC 배열에 추가한다.
(구현이 더 어렵지만, 활용도는 더 높다고 한다.)
"""

# 코사라주 알고리즘 활용
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

v, e = map(int, input().split())
graph = [[] for _ in range(v+1)]
reverse_graph = [[] for _ in range(v+1)]
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    reverse_graph[b].append(a)

def dfs(x):
    visited[x] = True
    for i in graph[x]:
        if visited[i]:
            continue
        dfs(i)
    stack.append(x)

def reverse_dfs(x, stack):
    visited[x] = True
    stack.append(x)
    for i in reverse_graph[x]:
        if visited[i]:
            continue
        reverse_dfs(i, stack)
    return stack

stack = []
visited = [False] * (v+1)
for i in range(1, v+1):
    if visited[i]:
        continue
    dfs(i)

visited = [False] * (v+1)
result = []
while stack:
    node = stack.pop()
    if visited[node]:
        continue
    scc = reverse_dfs(node, [])
    result.append(sorted(scc))
print(len(result))
answer = sorted(result)
for i in answer:
    print(*i, -1)

