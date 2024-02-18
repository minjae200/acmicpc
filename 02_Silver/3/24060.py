import sys
import copy
input = sys.stdin.readline

def merge(A, p, q, r):
    global count
    global result
    global K
    i = p
    j = q + 1
    temp = []

    while i <= q and j <= r:
        if A[i] < A[j]:
            push_number = A[i]
            i += 1
        else:
            push_number = A[j]
            j += 1
        temp.append(push_number)
    
    while i <= q:
        temp.append(A[i])
        i += 1

    while j <= r:
        temp.append(A[j])
        j += 1
            
    i = p
    t = 0
    while i <= r:
        A[i] = temp[t]
        count += 1
        if count == K:
            result = A[i]
        i += 1
        t += 1

def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)

result = -1
count = 0
N, K = map(int, input().strip().split())
numbers = list(map(int, input().strip().split()))
merge_sort(numbers, 0, len(numbers) - 1)
print(result)