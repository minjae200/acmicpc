A, B = map(int, input().split())
C = int(input())

if A + B < 2 * C:
    print(A+B)
else:
    print(A+B - 2 * C)