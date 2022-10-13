import sys
input = sys.stdin.readline

group = 0
while True:
    n = int(input())
    group += 1
    if n == 0:
        break
    names = []
    nasty = []
    for i in range(n):
        name_words = input().split()
        name = name_words[0]
        names.append(name)
        words = name_words[1:]

        for seq, word in enumerate(words):
            if word == 'N':
                idx = i - (seq + 1)
                if idx < 0:
                    idx += n
                nasty.append((idx, i))
    print(f'Group {group}')
    if not nasty:
        print('Nobody was nasty')
    else:
        for data in nasty:
            a, b = data[0], data[1]
            print(f'{names[a]} was nasty about {names[b]}')
    print('')