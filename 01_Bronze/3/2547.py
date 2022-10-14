
for _ in range(int(input())):
    input()
    n = int(input())
    candy = [ int(input()) for _ in range(n) ]
    total = sum(candy)
    if total % n == 0:
        print('YES')
    else:
        print('NO')