import sys
input = sys.stdin.readline
a, b = map(int, input().split())

data = [ 1 for _ in range(b-a+1) ]

i = 2
while i ** 2 <= b:
    mul = a // i ** 2
    while mul * (i**2) <= b:
        num = mul * (i ** 2) - a
        if 0 <= num <= b-a:
            data[num] = 0
        mul += 1
    i += 1
print(sum(data))
