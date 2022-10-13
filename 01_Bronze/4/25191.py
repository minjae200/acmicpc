n = int(input())
a, b = map(int, input().split())
a = a // 2
if a + b >= n:
    print(n)
else:
    print(a+b)