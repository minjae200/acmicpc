import sys
input = sys.stdin.readline

REGULAR = 8
SMALL = 3

regular = int(input())
small = int(input())

leftover = regular * REGULAR + small * SMALL - 28
print(leftover if leftover > 0 else 0)