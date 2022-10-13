import sys
input = sys.stdin.readline

board = input().strip()
ans = []
BY4 = 'AAAA'
BY2 = 'BB'
possible = True
for partial in board.split('.'):
    length = len(partial)
    if length % 2 != 0:
        possible = False
        break
    temp = ''
    while length > 0:
        if length >= 4:
            length -= 4
            temp += BY4
        else:
            length -= 2
            temp += BY2
    ans.append(temp)

if possible:
    print('.'.join(ans))
else:
    print(-1)