import bisect

n = int(input())
nums = [0] + list(map(int, input().split()))
dp = [0] * (n+1)
INF = int(1e9) + 1
arr = [-INF]

for i in range(1, n+1):
    if nums[i] > arr[-1]:
        arr.append(nums[i])
        dp[i] = len(arr) - 1
    else:
        dp[i] = bisect.bisect_left(arr, nums[i])
        arr[dp[i]] = nums[i]
print(len(arr) - 1)

idx = max(dp)  + 1
ans = []

for i in range(n, 0, -1):
    if dp[i] == idx - 1:
        ans.append(nums[i])
        idx = dp[i]
print(*ans[::-1])