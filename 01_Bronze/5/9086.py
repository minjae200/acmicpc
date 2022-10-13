import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    data = input().strip()
    print(''.join([data[0],data[-1]]))