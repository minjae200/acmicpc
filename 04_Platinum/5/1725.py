import sys
import math
input = sys.stdin.readline
MAX = int(1e9)

def init_tree(node, start, end):
    if start == end:
        tree[node] = nums[start]
        return tree[node]
    mid = (start + end) // 2
    tree[node] = min(init_tree(node*2, start, mid), init_tree(node*2+1, mid+1, end))
    return tree[node]

def solve(start, end):
    if start == end:
        return nums[start]
    
    mid = (start + end) // 2
    max_value = max(solve(start, mid), solve(mid+1, end))
    h = min(nums[mid], nums[mid+1])
    w = 2
    s = w * h
    i, j = mid, mid + 1
    while start < i or j < end:
        if j == end or start < i and nums[i-1] >= nums[j+1]:
            i -= 1
            w += 1
            h = min(h, nums[i])
        else:
            j += 1
            w += 1
            h = min(h, nums[j])
        s = max(s, w*h)
    max_value = max(max_value, s)
    return max_value

nums = [ int(input()) for _ in range(int(input()))]
tree_size = 1 << (math.ceil(math.log2(len(nums))) + 1)
tree = [0] * tree_size
init_tree(1, 0, len(nums) - 1)
print(solve(0, len(nums) - 1))