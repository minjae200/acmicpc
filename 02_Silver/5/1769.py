numbers = list(input().strip())

loop = 0
while len(numbers) != 1:
    total = sum(list(map(lambda x: int(x), numbers)))
    numbers = list(str(total))
    loop += 1
    
print(f'{loop}')
total = sum(list(map(lambda x: int(x), numbers)))
if total % 3 == 0:
    print('YES')
else:
    print('NO')