import sys
input = sys.stdin.readline

N = int(input())
S = list(map(int, input().strip().split()))

available = [False] * (20 * 100000 + 1)

def solve(index, total):
    if index == N:
        available[total] = True
        return
    solve(index + 1, total + S[index])
    solve(index + 1, total)

solve(0, 0)
for i in range(1, (20 * 100000 + 1)):
    if not available[i]:
        print(i)
        break

