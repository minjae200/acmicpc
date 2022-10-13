import sys
input = sys.stdin.readline

minguk = list(map(int, input().split()))
daehan = list(map(int, input().split()))

print(max(sum(minguk), sum(daehan)))