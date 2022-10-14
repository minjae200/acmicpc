board = [ list(map(int, input().split())) for _ in range(9) ]
temp = []
for i in range(9):
    temp.append(max(board[i]))
max_value = max(temp)
for i in range(9):
    for j in range(9):
        if board[i][j] == max_value:
            print(max_value)
            print(i+1, j+1)
            exit()