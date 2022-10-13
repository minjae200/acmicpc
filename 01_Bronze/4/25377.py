N = int(input())

wait = []
for _ in range(N):
    a, b = map(int, input().split())
    if a > b:
        continue
    wait.append(b)

wait.sort()
if not wait:
    print(-1)
else:
    print(wait[0])