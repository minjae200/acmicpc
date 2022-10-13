import sys
input = sys.stdin.readline

X = int(input())
cnt = 0
while X != 0:
    if X % 2 == 1:
        cnt += 1
    X = X // 2
print(cnt)