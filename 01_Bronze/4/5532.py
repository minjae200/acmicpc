L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

import math

homework = max(math.ceil(A/C), math.ceil(B/D))
print(L-homework)