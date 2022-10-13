L, R = input().split()
L_length = len(L)
R_length = len(R)
if L_length != R_length:
    print(0)
else:
    ans = 0
    for i in range(L_length):
        if L[i] != R[i]:
            break
        else:
            if L[i] == '8':
                ans += 1
    print(ans)
