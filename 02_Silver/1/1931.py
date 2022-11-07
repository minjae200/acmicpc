import sys
input = sys.stdin.readline

n = int(input())
meeting = []
for _ in range(n):
    start, end = map(int, input().split())
    meeting.append((start, end))

meeting.sort(key=lambda x: x[0])
meeting.sort(key=lambda x: x[1])

ans = 0
last = 0
for i in range(n):
    if last <= meeting[i][0]:
        ans += 1
        last = meeting[i][1]
print(ans)
