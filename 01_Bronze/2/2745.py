import sys, math
input = sys.stdin.readline
ary = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

N, B = map(str, input().split())
B = int(B)
idx = 1
total = 0

for data in N[::-1]:
    total += ary.index(data) * pow(B, idx-1)
    idx += 1

print(total)