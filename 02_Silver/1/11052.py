n = int(input())
p = list(map(int, input().split()))

dp = [-1] *(n + 1)
def solve(N):
    if N <= 0:
        return 0
    if dp[N] != -1:
        return dp[N]
    for i in range(1, N+1):
        dp[N] = max(dp[N], solve(N-i) + p[i-1])
    return dp[N]
print(solve(n))
