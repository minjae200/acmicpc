import sys
input = sys.stdin.readline

N = int(input().strip())
gu = list(map(int, input().strip().split()))

ans = 0

def solve(total):
    global gu
    global ans

    if len(gu) == 2:
        ans = max(ans, total)
        return

    for i in range(1, len(gu) - 1):
        partial = gu[i - 1] * gu[i + 1]
        v = gu.pop(i)
        solve(total + partial)
        gu.insert(i, v)
solve(0)
print(ans)