import sys
import itertools
import math
input = sys.stdin.readline

N = int(input().strip())
words = [ list(input().strip())[::-1] for _ in range(N) ]

alpha = [0] * 26

for word in words:
    for i, c in enumerate(word):
        alpha[ord(c) - ord('A')] += pow(10, i)

alpha.sort(reverse=True)

ans = 0
for i, a in enumerate(alpha[:9]):
    ans += (a * (9-i))
print(ans)