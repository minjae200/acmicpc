import sys
input = sys.stdin.readline

student = [False] * 31

for _ in range(28):
    student[int(input())] = True

for i in range(1, 31):
    if not student[i]:
        print(i)