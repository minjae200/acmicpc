import sys
import itertools
input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().strip().split()))
temp = list(map(int, input().strip().split()))

operator = []
for i, c in enumerate(temp):
    if c == 0:
        continue
    op = ''
    if i == 0:
        op = '+'
    elif i == 1:
        op = '-'
    elif i == 2:
        op = '*'
    else:
        op = '/'
    operator += [op] * c

A.sort()
result = []

def calc(perm):
    global operator
    ans = perm[0]
    for i, num in enumerate(perm[1:]):
        i = i + 1
        if operator[i-1] == '+':
            ans += perm[i]
        elif operator[i-1] == '-':
            ans -= perm[i]
        elif operator[i-1] == '*':
            ans *= perm[i]
        else:
            ans /= perm[i]
    return ans

for perm in itertools.permutations(A):
    result.append(calc(perm))

print(result)
print(max(result))
print(min(result))