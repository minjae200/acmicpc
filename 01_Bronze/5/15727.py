import sys
input = sys.stdin.readline

L = int(input())

print(L//5 + (1 if L%5 != 0 else 0))