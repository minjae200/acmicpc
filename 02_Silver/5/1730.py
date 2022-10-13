N = int(input())
commands = input().strip()

direct = {
    'U': { 'x': 0, 'y': -1, 'direction': 'vertical' },
    'D': { 'x': 0, 'y': 1, 'direction': 'vertical' },
    'R': { 'x': 1, 'y': 0, 'direction': 'horizontal' },
    'L': { 'x': -1, 'y': 0, 'direction': 'horizontal' }
}
x = 0
y = 0
horizontal = [[0] * N for _ in range(N)]
vertical = [[0] * N for _ in range(N)]
for command in commands:
    next_x = x + direct[command]['x']
    next_y = y + direct[command]['y']
    if (0 > next_x or next_x >= N) or (0 > next_y or next_y >= N):
        continue
    direction = direct[command]['direction']
    if direction == 'vertical':
        vertical[y][x] += 1
        vertical[next_y][next_x] += 1
    else:
        horizontal[y][x] += 1
        horizontal[next_y][next_x] += 1
    x = next_x
    y = next_y

board = [ ['.'] * N for _ in range(N) ]
for i in range(N):
    for j in range(N):
        if horizontal[i][j] >= 1 and vertical[i][j] >= 1:
            board[i][j] = '+'
        elif horizontal[i][j] >= 1:
            board[i][j] = '-'
        elif vertical[i][j] >= 1:
            board[i][j] = '|'
for line in board:
    print(''.join(line))