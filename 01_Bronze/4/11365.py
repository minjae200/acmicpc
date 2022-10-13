import sys
input = sys.stdin.readline


while True:
    line = input().strip()
    if line == 'END':
        break
    print(line[::-1])