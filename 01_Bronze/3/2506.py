n = int(input())
ox = list(map(int, input().split()))
score = 0
total = 0
for i in ox:
    if i == 1:
        score += 1
        total += score
    else:
        score = 0
print(total)