from re import L
import sys
input = sys.stdin.readline

N = int(input())

for i in range(1, 10):
    print('{} * {} = {}'.format(N, i, N*i))