import sys
input = sys.stdin.readline

def cut(start, n):
    global string
    if n == 1:
        return
    
    string[(start + n // 3):(start + n // 3 * 2)] = [' '] * (n//3)
    cut(start, n // 3)
    cut(start + n // 3 * 2, n // 3)

while True:
    try:
        N = int(input().strip())
        string = ['-'] * (3 ** N)
        cut(0, 3 ** N)
        print(''.join(string))
    except:
        break