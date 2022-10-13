a = input().strip()
n = int(input())
ans =0
for _ in range(n):
    data = input().strip()
    if data == a:
        ans += 1

print(ans)