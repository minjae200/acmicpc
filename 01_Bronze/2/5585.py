import sys
input = sys.stdin.readline

n = int(input())
remain = 1000 - n
coins = [500, 100, 50, 10, 5, 1]

ans = 0
index = 0
while remain > 0:
    if remain >= coins[index]:
        cnt = remain // coins[index]
        ans += cnt
        remain -= coins[index] * cnt
    else:
        index += 1
print(ans)