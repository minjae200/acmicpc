import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
sorted_a = sorted(a)
result = []
for i in range(n):
    index = sorted_a.index(a[i])
    result.append(index)
    sorted_a[index] = -1
print(*result)
