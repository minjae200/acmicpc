T = int(input())
for _ in range(T):
    problems = int(input())
    for _ in range(problems):
        numbers = list(map(int, input().split()))
        print(numbers[0] + numbers[1], numbers[0] * numbers[1])