import sys
input = sys.stdin.readline

N = int(input())
ans = 0
for _ in range(N):
    word = input().strip()
    group = True
    current = word[0]
    alpha = {current: 1}
    for i in word[1:]:
        if current != i:
            if i in alpha:
                group = False
                break
            alpha[i] = 1
            current = i
    ans += group
print(ans)