import sys
input = sys.stdin.readline

def merge_sort(start, end):
    global swap_count
    if start >= end:
        return
    mid = (start + end) // 2
    merge_sort(start, mid)
    merge_sort(mid+1, end)
    i, j = start, mid + 1
    temp = []
    while i <= mid and j <= end:
        if a[i] <= a[j]:
            temp.append(a[i])
            i += 1
        else:
            temp.append(a[j])
            j += 1
            swap_count += (mid - i + 1)
    
    if i <= mid:
        temp = temp + a[i:mid+1]
    if j <= end:
        temp = temp + a[j:end+1]
    
    for i in range(len(temp)):
        a[start + i] = temp[i]

swap_count = 0
n = int(input())
a = list(map(int, input().split()))
merge_sort(0, n-1)
print(swap_count)