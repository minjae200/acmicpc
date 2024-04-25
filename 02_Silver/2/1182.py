import sys
input = sys.stdin.readline

N, S = map(int, input().strip().split())
array = list(map(int, input().strip().split()))

ans = 0
def solve(index, total):
    global ans
    if index == N:
        if total == S:
            ans += 1
        return
    solve(index + 1, total + array[index])
    solve(index + 1, total)

solve(0, 0)
if S == 0:
    ans -= 1
print(ans)