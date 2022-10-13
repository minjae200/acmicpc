import sys
input = sys.stdin.readline

num = int(input())
for i in range(num):
    a, b, c, d = map(int, input().split())
    total = b + c + d
    if total < 55:
        print(f'{a} {total} FAIL')
    elif b / 35 < 0.3:
        print(f'{a} {total} FAIL')
    elif c / 25 < 0.3:
        print(f'{a} {total} FAIL')
    elif d / 40 < 0.3:
        print(f'{a} {total} FAIL')
    elif d / 40 >= 0.3 and c / 25 >= 0.3 and b / 35 >= 0.3:
        print(f'{a} {total} PASS')