
B1 = input().strip()
B2 = input().strip()

ans = bin(int(B1, 2) * int(B2, 2))[2:]
print(ans)