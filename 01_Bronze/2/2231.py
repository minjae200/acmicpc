import sys
input = sys.stdin.readline

n = int(input())
ans = 0
start = n - len(str(n)) * 9
for i in range(max(1, start), n+1):
    data = list(map(int, str(i)))
    total = i + sum(data)
    if total == n:
        ans = i
        break
print(ans)