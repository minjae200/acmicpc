import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
A = [ list(map(int, input().strip().split())) for _ in range(N) ]

M, K = map(int, input().strip().split())
B = [ list(map(int, input().strip().split())) for _ in range(M) ]

C = [[ 0 for _ in range(K) ] for _ in range(N) ]

for n in range(N):
    for k in range(K):
        for m in range(M):
            C[n][k] += A[n][m] * B[m][k]

for i in C:
    for j in i:
        print(j, end=' ')
    print()