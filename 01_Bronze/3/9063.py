import sys
input = sys.stdin.readline

N = int(input().strip())
X = []
Y = []
for _ in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)
print((max(X) - min(X)) * (max(Y) - min(Y)))