import sys
input = sys.stdin.readline

while True:
    n = int(input().strip())
    if n == -1:
        break
    arr = []
    for i in range(1, n):
        if n % i == 0:
            arr.append(i)
    if sum(arr) == n:
        arr = list(map(str, arr))
        print(f'{n} = {" + ".join(arr)}')
    else:
        print(f'{n} is NOT perfect.')