n = int(input())
nums = list(map(int, input().split()))
result = [nums[0]]
for i in range(len(nums) - 1):
    result.append(max(result[i] + nums[i+1], nums[i+1]))
print(max(result))