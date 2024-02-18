import sys
input = sys.stdin.readline

count = 0
def recursive(s, l, r):
    global count
    count += 1
    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        return recursive(s, l+1, r-1)

def isPalindrome(s):
    return recursive(s, 0, len(s)-1)

T = int(input().strip())
for _ in range(T):
    s = input().strip()
    count = 0
    print(isPalindrome(s), count)