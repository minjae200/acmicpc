n = int(input())

factorial = [1]
value = 1
for i in range(1, 21):
    value *= i
    factorial.append(value)

if n == 0:
    print('NO')
else:
    for i in range(20, -1, -1):
        if n >= factorial[i]:
            n -= factorial[i]
    
    print('YES' if n == 0 else 'NO')