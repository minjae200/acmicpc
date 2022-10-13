import sys
input = sys.stdin.readline

stack = []
n = int(input())
buildings = list(map(int, input().split()))
answer = [0] * n

for i in range(n):
    building = buildings[i]
    while stack:
        if stack[-1][1] > building:
            answer[i] = stack[-1][0] + 1
            break
        else:
            stack.pop()
    stack.append((i, building))

print(*answer)