import sys
input = sys.stdin.readline
N = int(input().strip())

def recursive(n):
    if n == 0:
        return 1
    return n * recursive(n - 1)

print(recursive(N))
