n = int(input())
p = int(input())

if n >= 20:
    price_01 = int(p * 0.75)
    price_02 = max(0, p-2000)
    print(min(price_01, price_02))
elif n >= 15:
    price_01 = max(0, p-2000)
    price_02 = int(p * 0.9)
    print(min(price_01, price_02))
elif n >= 10:
    price_01 = int(p * 0.9)
    price_02 = max(0, p-500)
    print(min(price_01, price_02))
else:
    print(max(0, p-500))