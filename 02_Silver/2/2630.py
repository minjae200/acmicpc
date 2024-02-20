import sys
input = sys.stdin.readline

N = int(input().strip())
paper = [ list(map(int, input().strip().split())) for _ in range(N) ]

white = 0
blue = 0

def recursive(x, y, N):
    global white
    global blue
    color = paper[x][y]
    for i in range(x, x + N):
        for j in range(y, y + N):
            if color != paper[i][j]:
                recursive(x, y, N//2)
                recursive(x, y + N//2, N//2)
                recursive(x + N//2, y, N//2)
                recursive(x + N//2, y + N//2, N//2)
                return
    if color == 0:
        white += 1
    else:
        blue += 1

recursive(0, 0, N)
print(white)
print(blue)