g, p, t = map(int, input().split())

indivisual = g * p
group = g + p * t

if indivisual > group:
    print('2')
elif indivisual < group:
    print('1')
else:
    print('0')