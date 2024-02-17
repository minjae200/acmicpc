import sys
input = sys.stdin.readline

N, M = map(int, input().split())

basket = [ i for i in range(1, N+1) ]
for _ in range(M):
    i, j = map(int, input().split())
    basket[i-1:j] = reversed(basket[i-1:j])

print(*basket)