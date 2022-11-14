scores = list(map(int, input().split()))
total = sum(scores)

if total < 100:
    print('none')
else:
    max_score = [100, 100, 200, 200, 300, 300, 400, 400, 500]

    hacker = False
    for i, j in zip(max_score, scores):
        if i < j:
            hacker = True
            break
    print('hacker') if hacker else print('draw')