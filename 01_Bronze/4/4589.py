import sys
input = sys.stdin.readline

N = int(input())

print('Gnomes:')
for _ in range(N):
    numbers = list(map(int, input().split()))

    sorted_numbers = sorted(numbers)
    reversed_numbers = sorted(numbers, reverse=True)

    if numbers == sorted_numbers or numbers == reversed_numbers:
        print('Ordered')
    else:
        print('Unordered')