num = int(input())

for i in range(num):
    ship, speed, day = map(int, input().split())
    ducats = 0
    for _ in range(ship):
        distance, numDucats = map(int, input().split())
        if (day * speed >= distance):
            ducats += numDucats
    print(f'Data Set {i+1}:')
    print(ducats)
    print()