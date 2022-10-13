import sys
input = sys.stdin.readline

N = int(input())
K = int(input())

prime = [ 0 for _ in range(N+1) ]
for i in range(2, N+1):
    if prime[i] == 0:
        for j in range(i, N+1, i):
            if j % i == 0:
                prime[j] = max(prime[j], i)
ans = 0
for data in prime[1:]:
    if data <= K:
        ans += 1
print(ans)
