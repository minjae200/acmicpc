import sys
input = sys.stdin.readline

total = 0
for _ in range(4):
    total += int(input())

hours = total // 60
minutes = total % 60
print(hours)
print(minutes)