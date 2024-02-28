import sys
input = sys.stdin.readline

N = int(input().strip())
paper = [ list(map(int, input().strip().split())) for _ in range(N) ]


ans = [0, 0, 0, 0]

def divide(x, y, n):
    number = paper[x][y]
    diff = False
    for i in range(x, x + n):
        for j in range(y, y + n):
            if number != paper[i][j]:
                diff = True
                break
        if diff:
            break
    
    if diff:
        n = n // 3
        divide(x, y, n)
        divide(x + n, y, n)
        divide(x + 2 * n, y, n)
        divide(x, y + n, n)
        divide(x, y + 2 * n , n)
        divide(x + n, y + n, n)
        divide(x + 2 * n, y + n , n)
        divide(x + n, y + 2 * n , n)
        divide(x + 2 * n, y + 2 * n , n)
    else:
        ans[number + 1] += 1


divide(0, 0, N)

print(ans[0])
print(ans[1])
print(ans[2])