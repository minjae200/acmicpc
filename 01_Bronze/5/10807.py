import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
v = int(input())

from collections import Counter

counter = Counter(numbers)
print(counter[v])
