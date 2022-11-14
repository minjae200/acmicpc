import sys
input = sys.stdin.readline

q = []
for _ in range(int(input())):
    commands = input().strip().split()
    if len(commands) == 1:
        command = commands[0]

        if command == 'front':
            if not q:
                print(-1)
            else:
                print(q[0])
        elif command == 'back':
            if not q:
                print(-1)
            else:
                print(q[-1])
        elif command == 'size':
            print(len(q))
        elif command == 'empty':
            print(1) if not q else print(0)
        elif command == 'pop':
            if not q:
                print(-1)
            else:
                print(q.pop(0))
    else:
        command = commands[0]
        number = commands[1]
        if command == 'push':
            q.append(number)
        
    