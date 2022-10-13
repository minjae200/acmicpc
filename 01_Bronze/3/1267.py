n = int(input())
costs = list(map(int, input().split()))

M = 0
Y = 0
for cost in costs:
    Y += ((cost // 30) + 1 ) * 10
    M += ((cost // 60) + 1 ) * 15

if M < Y:
    print('M {}'.format(M))
elif Y < M:
    print('Y {}'.format(Y))
else:
    print('Y M {}'.format(M))