import sys
input = sys.stdin.readline

class Shark:
    def __init__(self, size, speed, intel):
        self.size = size
        self.speed = speed
        self.intel = intel

    def __ge__(self, other):
        if self.size >= other.size and self.speed >= other.speed and self.intel >= other.intel:
            return True
        else:
            return False
    
    def __eq__(self, other):
        if self.size == other.size and self.speed == other.speed and self.intel == other.intel:
            return True
        else:
            return False

n = int(input())
sharks = []
for _ in range(n):
    size, speed, intel = map(int, input().split())
    sharks.append(Shark(size, speed, intel))

adj = [[] for _ in range(n)] # 어떤상어가 무슨 상어를 잡아먹을 수 있는지에 대한 정보

for i in range(len(sharks) - 1):
    for j in range(i+1, len(sharks)):
        if sharks[i] == sharks[j]:
            adj[i].append(j)
        elif sharks[i] >= sharks[j]:
            adj[i].append(j)
        elif sharks[j] >= sharks[i]:
            adj[j].append(i)

occupy = [-1] * n
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

for _ in range(2):
    for i in range(n):
        visited = [False] * n
        if dfs(i):
            matching += 1

print(n - matching)
