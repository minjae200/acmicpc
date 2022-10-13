n = int(input())
dice = list(map(int, input().split()))

side_1 = 4 * (n-2) * (n-1) + (n-2) ** 2
side_2 = 4 * (n-2) + 4 * (n-1)
side_3 = 4

if n == 1:
    dice.sort()
    result = sum(dice[:5])
else:
    tmp = []
    tmp.append(min(dice[0], dice[5]))
    tmp.append(min(dice[1], dice[4]))
    tmp.append(min(dice[2], dice[3]))
    tmp.sort()

    min_1 = tmp[0]
    min_2 = tmp[0] + tmp[1]
    min_3 = tmp[0] + tmp[1] + tmp[2]

    result = side_1 * min_1 + side_2 * min_2 + side_3 * min_3
print(result)