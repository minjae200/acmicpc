n = int(input())
a = list(map(int, input().split()))
v = 0
for i in a:
    v = round((1 - (1 - v / 100) * (1 - i / 100)) * 100, 6)
    print(v)