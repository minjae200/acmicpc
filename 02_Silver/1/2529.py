import sys
import itertools
input = sys.stdin.readline

k = int(input().strip())
a = list(map(str, input().strip().split()))

small = [ num for num in range(k+1) ]
big = [ num for num in range(9, 9-(k+1), -1) ]


def check(numbers):
    global a
    for i, number in enumerate(numbers[:-1]):
        if a[i] == '<' and numbers[i] > numbers[i+1]:
            return False
        elif a[i] == '>' and numbers[i] < numbers[i+1]:
            return False
    return True

for permutation in itertools.permutations(big):
    if check(permutation):
        print(*permutation, sep='')
        break

for permutation in itertools.permutations(small):
    if check(permutation):
        print(*permutation, sep='')
        break
