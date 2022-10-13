a, b, c = map(int, input().split())

if a + b == c or b + c == a or a + c == b:
    print(1)
elif a * b == c or b * c == a or a * c == b:
    print(2)
else:
    print(3)