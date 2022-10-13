import sys
import math
input = sys.stdin.readline

MAX = int(1e9)
MIN = 0

n, m = map(int, input().split())
h = int(math.ceil(math.log2(n)))
tree_size = 1 << (h+1)
arr = []
for _ in range(n):
    arr.append(int(input().strip()))

def initTree(node, start, end):
    if start == end:
        tree[node] = (arr[start], arr[start])
        return tree[node]
    mid = (start + end) // 2

    left_tree = initTree(node*2, start, mid)
    right_tree = initTree(node*2+1, mid+1, end)
    tree[node] = (min(left_tree[0], right_tree[0]), max(left_tree[1], right_tree[1]))
    return tree[node]

tree = [(0, 0)] * tree_size
initTree(1, 0, n-1)

def query(node, start, end, left, right):
    if start > right or end < left:
        return (MAX, MIN)
    if left <= start and end <= right:
        return tree[node]
    
    mid = (start + end) // 2
    left_tree = query(node*2, start, mid, left, right)
    right_tree = query(node*2+1, mid+1, end, left, right)
    return (min(left_tree[0], right_tree[0]), max(left_tree[1], right_tree[1]))

for _ in range(m):
    a, b = map(int, input().split())
    value = query(1, 0, n-1, a-1, b-1)
    print(f'{value[0]} {value[1]}')