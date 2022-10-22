
result = []
for i in range(1, 6):
    if 'FBI' in input().strip():
        result.append(i)

if not result:
    print('HE GOT AWAY!')
else:
    print(*result)