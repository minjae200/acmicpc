import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lines = [ list(input().strip()) for _ in range(N)]

for line in lines:
    print(''.join(list(reversed(line))))
