a, b = map(int, input().split())
n = int(input())
for _ in range(n):
    usage = int(input())
    price = 0

    if usage <= 1000:
        price = usage * a
    else:
        price = 1000 * a + (usage - 1000) * b
    print(usage, price)