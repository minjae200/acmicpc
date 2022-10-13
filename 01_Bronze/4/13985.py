sent = input().strip().split(' ')

a = int(sent[0])
b = int(sent[2])
c = int(sent[-1])

if (a+b == c):
    print('YES')
else:
    print('NO')