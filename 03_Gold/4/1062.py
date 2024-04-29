import sys
input = sys.stdin.readline

N, K = map(int, input().strip().split())
words = [0 for _ in range(N)]
for i in range(N):
    for s in input().strip():
        words[i] = words[i] | (1 << (ord(s) - ord('a')))

def count(mask):
    cnt = 0
    global words
    for word in words:
        if (word & ((1 << 26) - 1 - mask) == 0):
            cnt += 1
    return cnt

def go(index, k, mask):
    if k < 0:
        return 0
    if index == 26:
        return count(mask)
    
    ans = 0
    t1 = go(index + 1, k - 1, mask | (1 << index))
    ans = max(ans, t1)
    if index != (ord('a') - ord('a')) and index != (ord('n') - ord('a')) and index != (ord('t') - ord('a')) and index != (ord('i') - ord('a')) and index != (ord('c') - ord('a')):
        t1 = go(index + 1, k, mask)
        ans = max(ans, t1)
    return ans


print(go(0, K, 0))