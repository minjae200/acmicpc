import sys
input = sys.stdin.readline

n, m = map(int, input().split())

A = list(map(int, input().split()))

left, right = 0, 1
ans = 0

while right <= n and left <= right:
    total = sum(A[left:right])
    if total == m:
        ans += 1
        left += 1
        right += 1
        continue

    if total < m:
        right += 1
    else:
        left += 1
print(ans)