import sys
from tokenize import Double
input = sys.stdin.readline

a, b = map(int, input().split())

defense = a - a * b / 100
print(1 if defense < 100.0 else 0)