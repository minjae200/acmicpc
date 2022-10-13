import sys
input = sys.stdin.readline
score = []
for _ in range(6):
    score.append(int(input().strip()))
a = sorted(score[:4], reverse=True)
b = sorted(score[4:], reverse=True)
print(sum(a[:3]) + b[0])