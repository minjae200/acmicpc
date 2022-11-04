import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
broken = list(map(int, input().split()))

ans = abs(100 - n)
MAX_N = 500000
for nums in range(2 * MAX_N + 1):
    possible = True
    for num in str(nums):
        if int(num) in broken:
            possible = False
            break
    if possible:
        ans = min(ans, abs(int(nums)-n) + len(str(nums)))
print(ans)