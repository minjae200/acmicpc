import sys, copy
input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    priority = list(map(int, input().split()))
    tmp = []
    for i, prio in enumerate(priority):
        tmp.append((i, prio))

    find = False
    ans = 0
    while not find:
        ans += 1
        max_prio = max(tmp, key=lambda x: x[1])
        for item in copy.deepcopy(tmp):
            index = item[0]
            prio = item[1]
            tmp.remove(item)
            if item == max_prio:
                if index == m:
                    find = True
                break
            tmp.append(item)

    print(ans)