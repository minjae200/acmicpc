import copy
n = int(input())
first = list(input())
result = copy.deepcopy(first)

for i in range(1, n):
    data = input()
    for ind, j in enumerate(data):
        if first[ind] != j:
            result[ind] = '?'

print(*result, sep='')