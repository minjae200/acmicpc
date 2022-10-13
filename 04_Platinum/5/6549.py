import sys
import math
input = sys.stdin.readline
MAX = int(1e9)


def init_tree(node, start, end):
    if start == end:
        tree[node] = histograms[start]
        return tree[node]
    mid = (start + end) // 2
    tree[node] = min(init_tree(node*2, start, mid), init_tree(node*2+1, mid+1, end))
    return tree[node]

def solve(start, end):
    if start == end:
        return histograms[start]
    
    mid = (start + end) // 2
    max_value = max(solve(start, mid), solve(mid+1, end))

    h = min(histograms[mid], histograms[mid+1])
    w = 2
    s = w * h
    i, j = mid, mid + 1
    while start < i or j < end:
        if j == end or start < i and histograms[i-1] >= histograms[j+1]:
            i -= 1
            w += 1
            h = min(h, histograms[i])
        else:
            j += 1
            w += 1
            h = min(h, histograms[j])
        s = max(s, w*h)
    max_value = max(max_value, s)
    return max_value

while True:
    data = list(map(int, input().split()))
    if data[0] == 0:
        break
    histograms = data[1:]

    b = math.ceil(math.log2(data[0])) + 1
    tree_size = 1 << b
    tree = [0] * tree_size
    init_tree(1, 0, len(histograms)-1)
    print(solve(0, len(histograms) - 1))