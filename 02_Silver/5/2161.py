from collections import deque


from collections import deque

n = int(input())
cards = [i for i in range(1, n+1)]

q = deque(cards)
seq = []
while q:
    card = q.popleft()
    seq.append(card)
    if q:
        next_card = q.popleft()
        q.append(next_card)
print(*seq)