import sys
input = sys.stdin.readline

N = input().strip()

N = int(N, 2) * 17
print(bin(N)[2:])