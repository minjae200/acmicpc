import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    commands = list(input().strip())
    n = int(input())
    data = list(filter(lambda x: x, input().strip().replace('[', '').replace(']', '').split(',')))
    data = deque(data)
    reverse = False
    result = True
    for command in commands:
        if command == 'R':
            reverse = not reverse
        elif command == 'D':
            if not data:
                result = False
                break
            if reverse:
                data.pop()
            else:
                data.popleft()

    if result:
        if reverse:
            data = list(data)[::-1]
        else:
            data = list(data)
        print('[{}]'.format(','.join(data)))
    else:
        print('error')