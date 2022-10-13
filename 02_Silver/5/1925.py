import math
import sys
input = sys.stdin.readline

a_x, a_y = map(int, input().split())
b_x, b_y = map(int, input().split())
c_x, c_y = map(int, input().split())

len_ab = (a_x-b_x) ** 2 + (a_y-b_y) ** 2
len_ac = (a_x-c_x) ** 2 + (a_y-c_y) ** 2
len_bc = (b_x-c_x) ** 2 + (b_y-c_y) ** 2

length2 = [len_ab, len_ac, len_bc]
length2.sort()
length = [math.sqrt(len_ab), math.sqrt(len_ac), math.sqrt(len_bc)]
length.sort()

if length[2] >= length[0] + length[1]:
    print('X')
elif (length[2] == length[0]) and (length[2] == length[1]) and (length[1] == length[0]):
    print('JungTriangle')
elif (length[2] == length[0]) or (length[2] == length[1]) or (length[1] == length[0]):
    if length2[0] + length2[1] < length2[2]:
        print('Dunkak2Triangle')
    elif length2[0] + length2[1] == length2[2]:
        print('Jikkak2Triangle')
    else:
        print('Yeahkak2Triangle')
else:
    if length2[0] + length2[1] < length2[2]:
        print('DunkakTriangle')
    elif length2[0] + length2[1] == length2[2]:
        print('JikkakTriangle')
    else:
        print('YeahkakTriangle')
