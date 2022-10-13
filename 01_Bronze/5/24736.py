import sys
input = sys.stdin.readline

ans = []
for _ in range(2):
    T, F, S, P, C = map(int, input().split())
    ans.append(T*6 + F*3 + S*2 + 1*P + 2*C)
print(*ans)