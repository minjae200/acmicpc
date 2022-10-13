import sys
input = sys.stdin.readline

N = int(input())
data = []
for _ in range(N):
    a, b = map(int, input().split())
    data.append((a,b))

data.sort(key=lambda x: x[0])

cache = [1] * (N+1)
for i in range(N):
    a = data[i]
    for j in range(i):
        b = data[j]
        if a[1] > b[1]:
            cache[i] = max(cache[i], cache[j] + 1)

print(N - max(cache))