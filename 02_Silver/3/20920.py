import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
note = {}
for _ in range(N):
    word = input().strip()
    if len(word) < M:
        continue
    if word not in note:
        note[word] = 0
    note[word] += 1

words = list(note.keys())

def cmp(word):
    return (-note[word], -len(word), word)

words.sort(key=cmp)
print(*words, sep='\n')