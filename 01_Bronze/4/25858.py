n, reward = map(int, input().split())
solve = [ int(input()) for _ in range(n) ]
total = sum(solve)
daller = reward // total
for i in solve:
    print(daller * i)


