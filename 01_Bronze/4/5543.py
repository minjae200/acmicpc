import sys
input = sys.stdin.readline

burger = []
drink = []

for _ in range(3):
    burger.append(int(input()))
for _ in range(2):
    drink.append(int(input()))

burger.sort()
drink.sort()
print(burger[0] + drink[0] - 50)