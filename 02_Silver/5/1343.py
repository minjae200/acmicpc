import sys
input = sys.stdin.readline
PolyominoBy4 = 'AAAA'
PolyominoBy2 = 'BB'

board = input().strip()
possible = True
ans = []
for partial in board.split('.'):
    length = len(partial)
    if length % 2 != 0:
        possible = False
        break
    cntBy4 = length // 4
    length -= cntBy4 * 4
    cntBy2 = length // 2
    length -= cntBy2 * 2
    ans.append((PolyominoBy4 * cntBy4) + (PolyominoBy2 * cntBy2))
print('.'.join(ans)) if possible else print(-1)