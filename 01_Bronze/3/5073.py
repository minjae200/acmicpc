import sys
input = sys.stdin.readline


while True:
    tri = list(map(int, input().split()))
    if sum(tri) == 0:
        break

    tri.sort()
    set_tri = set(tri)
    if tri[2] >= (tri[0] + tri[1]):
        print('Invalid')
    elif len(set_tri) == 1:
        print('Equilateral')
    elif len(set_tri) == 2:
        print('Isosceles')
    else:
        print('Scalene')