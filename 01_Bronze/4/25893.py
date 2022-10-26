for _ in range(int(input())):
    a, b, c = map(int, input().split())
    print(a, b, c, sep=' ')
    if a < 10 and b < 10 and c < 10:
        print('zilch')
    elif a >= 10 and b >= 10 and c >= 10:
        print('triple-double')
    elif (a >= 10 and b >= 10) or (b >= 10 and c >= 10) or (a >= 10 and c>=10):
        print('double-double')
    else:
        print('double')
    print()