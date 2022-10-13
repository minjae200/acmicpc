import sys
input = sys.stdin.readline
Ax, Ay, Az = map(int, input().split())
Cx, Cy, Cz = map(int, input().split())

print(Cx-Az, Cy // Ay, Cz-Ax)