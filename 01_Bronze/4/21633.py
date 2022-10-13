amount = int(input())

if (amount * 0.01 + 25) < 100:
    print(100)
elif (amount * 0.01 + 25) > 2000:
    print(2000)
else:
    print(amout * 0.01 + 25)