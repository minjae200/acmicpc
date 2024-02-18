import sys
input = sys.stdin.readline

N = int(input().strip())
people = ['ChongChong']

for _ in range(N):
    A, B = input().strip().split()
    if A in people:
        people.append(B)
    elif B in people:
        people.append(A)
result = list(set(people))
print(len(result))