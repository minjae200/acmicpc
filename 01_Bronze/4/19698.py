N, W, H, L = map(int, input().split())

cow = min(N, (W //L) * (H//L))

print(cow)