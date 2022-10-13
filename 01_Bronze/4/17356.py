import math
a, b = map(int, input().split())

m = (b-a) / 400

print( 1 / (1 + math.pow(10, m)))