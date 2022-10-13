import sys
input = sys.stdin.readline

T = 0
while True:
    n = int(input())
    if n == 0:
        break
    T += 1
    students = ['']
    for _ in range(n):
        students.append(input().strip())
    info = {}
    for _ in range(2*n-1):
        number, AorB = list(input().split())
        number = int(number)
        if number not in info:
            info[number] = 0
        info[number] += 1

    # print(info)

    res = students[[i for i in range(1, n+1) if info[i] != 2][0]]
    print(f'{T} {res}')