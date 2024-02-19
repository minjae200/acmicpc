import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
A = list(map(int, input().strip().split()))
r = [0] * M

prefix_sum = 0
for num in A:
    prefix_sum += num
    r[prefix_sum % M] += 1

answer = r[0]
for i in range(M):
    answer += r[i] * (r[i]-1) // 2
print(answer)