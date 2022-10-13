K, L = map(int, input().split())
good = True
for i in range(2, L):
    if K % i == 0:
        print('BAD', i)
        good = False
        break
if good:
    print('GOOD')