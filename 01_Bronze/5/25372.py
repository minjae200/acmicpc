import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    if 6 <= len(input().strip()) <= 9:
        print('yes')
    else:
        print('no')
