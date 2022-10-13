import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    a, b = input().split()
    result = True
    for i in range(len(a)):
        if a[i] != b[i]:
            result = False
            break
    if result:
        print('OK')
    else:
        print('ERROR')