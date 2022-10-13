add, sub = map(int, input().split())

if (add+sub) % 2 != 0 or add+sub < 0 or add-sub < 0:
    print(-1)
else:
    x = (add+sub)//2
    y = add-x
    print(max(x, y), min(x, y))
