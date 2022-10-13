import math
N = int(input())

prime = [True] * (1001)
prime[1] = False
for i in range(2, int(math.sqrt(1001))):
    if not prime[i]:
        continue
    for j in range(i+i, 1001, i):
        prime[j] = False

total = 0
for data in list(map(int, input().split())):
    total += prime[data]

print(total)