data = sorted(list(map(int, input().split())))

if data[0] == data[1]:
    print('S')
elif data[1] == data[2]:
    print('S')
elif data[0] + data[1] == data[2]:
    print('S')
else:
    print('N')