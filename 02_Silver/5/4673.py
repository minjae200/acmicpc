num = set(range(1, 10000))
tmp = set()

for i in range(1, 10001):
    tmp.add(i + sum(map(int, str(i))))

self_num = sorted(num - tmp)
print(*self_num, sep='\n')