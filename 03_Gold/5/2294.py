import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [0]
for _ in range(n):
    coins.append(int(input()))

cache = [int(1e9)] * 10001
cache[0] = 0
for i in range(1, k+1):
    for j in range(1, n+1):
        if (i-coins[j] >= 0) and (cache[i-coins[j]] != int(1e9)):
            cache[i] = min(cache[i], cache[i-coins[j]]+1)
print(cache[k] if cache[k] != int(1e9) else -1)