import sys
input = sys.stdin.readline

alpha = ['a', 'e', 'i', 'o', 'u']

while True:
    count = 0
    data = input().strip().lower()
    if data == '#':
        break
    for i in data:
        if i in alpha:
            count += 1
    print(count)