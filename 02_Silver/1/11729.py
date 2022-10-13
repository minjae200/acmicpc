def hanoi(n, a, b, c):
    if n == 1:
        result.append((a, c))
    else:
        hanoi(n-1, a, c, b)
        result.append((a, c))
        hanoi(n-1, b, a, c)

n = int(input())
result = []
hanoi(n, 1, 2, 3)
print(len(result))
for item in result:
    print(f'{item[0]} {item[1]}')