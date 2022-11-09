import sys
input = sys.stdin.readline

A, B, C, D = map(int, input().split())
times = list(map(int, input().split()))
for time in times:
    attacked = 0
    if 0 < time % (A+B) <= A:
        attacked += 1
    if 0 < time % (C+D) <= C:
        attacked += 1
    print(attacked)