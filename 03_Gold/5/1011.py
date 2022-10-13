import sys, math
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    x, y = map(int, input().split())
    distance = y - x
    
    num = math.floor(math.sqrt(distance))
    num_square = num ** 2
    increase_num = math.sqrt(num_square)

    if distance > num_square + increase_num:
        count = 2 * num + 1
    elif distance > num_square and distance <= num_square + increase_num:
        count = 2 * num
    elif distance == num_square:
        count = 2 * num - 1

    if distance < 4:
        count = distance

    print(count)