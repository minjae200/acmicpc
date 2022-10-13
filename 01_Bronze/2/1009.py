for _ in range(int(input())):
    a, b = map(int, input().split())
    data = int(pow(a, b, 10))
    print(10) if data == 0 else print(data)