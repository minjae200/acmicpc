import sys
input = sys.stdin.readline

N = int(input())
data = ['long'] * (N//4 + (1 if N%4 else 0)) + ['int']
print(*data)