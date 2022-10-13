N, M = map(int, input().split())
box = 0
weight = 0
if N != 0:
    books = list(map(int, input().split()))
    for book in books:
        if weight + book > M:
            weight = book
            box += 1
            continue
        elif weight + book == M:
            weight = 0
            box += 1
            continue
        weight += book
print(box + (weight != 0))