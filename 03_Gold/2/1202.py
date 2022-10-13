import sys, heapq
input = sys.stdin.readline
n, k = map(int, input().split())
array = []
for _ in range(n):
    m, v = map(int, input().split())
    heapq.heappush(array, [m,v])
bags = [int(input()) for _ in range(k)]
bags.sort()

q = []
ans = 0
for bag in bags:
    while array and bag >= array[0][0]:
        m, v = heapq.heappop(array)
        heapq.heappush(q, -v)
    if q:
        ans -= heapq.heappop(q)
    elif not array:
        break
print(ans)