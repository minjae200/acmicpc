total = 0
for _ in range(6):
    a = input().strip()

    if a == 'W':
        total += 1

if total == 5 or total == 6:
    print(1)
elif total == 3 or total == 4:
    print(2)
elif total== 1 or total == 2:
    print(3)
else:
    print(-1)