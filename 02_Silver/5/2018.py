N = int(input())

surfix = [0] * (N+1)
for i in range(1, N+1):
    surfix[i] = surfix[i-1] + i
start = 0
end = 0

partial = 0
ans = 0
while start <= N and end <= N:
    partial = surfix[end] - surfix[start]
    if partial == N:
        ans += 1
        partial = 0
        end += 1
    elif partial < N:
        end += 1
    else:
        start += 1
print(ans)