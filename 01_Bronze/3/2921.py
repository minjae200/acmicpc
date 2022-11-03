import sys
input = sys.stdin.readline

n = int(input())
total = 0
for i in range(0, n + 1):
    for j in range(i, n + 1):
        total += i + j
print(total)