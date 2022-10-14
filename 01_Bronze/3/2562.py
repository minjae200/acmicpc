nums = [ int(input()) for _ in range(9) ]
max_value = max(nums)
index = nums.index(max_value)
print(max_value, index + 1, sep='\n')