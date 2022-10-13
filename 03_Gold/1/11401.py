import sys
input = sys.stdin.readline

N, K = map(int, input().split())
MOD = 1000000007

def factorial(N):
    n = 1
    for i in range(2, N+1):
        n = (n * i) % MOD
    return n

def square(n, k):
    if k == 0:
        return 1
    elif k == 1:
        return n
    tmp = square(n, k//2)
    if k % 2:
        return tmp * tmp * n % MOD
    else:
        return tmp * tmp % MOD

top = factorial(N)
bot = factorial(N-K) * factorial(K) %  MOD
# 페르마의 소정리
print(top * square(bot, MOD-2) % MOD)