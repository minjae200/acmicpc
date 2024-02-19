import sys
input = sys.stdin.readline

string = input().strip()

prefix_sum = [[0] * 26 for _ in range(len(string) + 1)]
for idx, c in enumerate(string):
    for j in range(26):
        prefix_sum[idx + 1][j] = prefix_sum[idx][j]
    prefix_sum[idx + 1][ord(c) - ord('a')] += 1

n = int(input().strip())
for _ in range(n):
    char, start, end = input().strip().split()
    index = ord(char) - ord('a')
    print(prefix_sum[int(end) + 1][index] - prefix_sum[int(start)][index])