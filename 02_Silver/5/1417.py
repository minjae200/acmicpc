import re


N = int(input())
votes = []
if N == 1:
    print(0)
else:
    for _ in range(N):   
        votes.append(int(input()))
    dasom = votes[0]
    votes = votes[1:]
    votes.sort(reverse=True)
    count = 0
    while votes[0] >= dasom:
        dasom += 1
        votes[0] -= 1
        count += 1
        votes.sort(reverse=True)
    print(count)