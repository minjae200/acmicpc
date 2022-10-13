import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrixA = [ list(map(int,input().split())) for _ in range(N) ]
matrixB = [ list(map(int,input().split())) for _ in range(N) ]

for i in range(N):
    for j in range(M):
        print(matrixA[i][j] + matrixB[i][j], end=' ')
    print()