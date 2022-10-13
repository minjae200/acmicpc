import re
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    signal = input().strip()
    pattern = re.compile('(100+1+|01)+')
    if pattern.fullmatch(signal):
        print('YES')
    else:
        print('NO')