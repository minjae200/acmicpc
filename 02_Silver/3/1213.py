import sys
from collections import Counter
input = sys.stdin.readline

words = list(input().strip())
words.sort()
counter = Counter(words)

odds = list(filter(lambda x: (x[1] % 2) == 1, counter.items()))
center = ''
for odd in odds:
    center += odd[0]
    words.remove(odd[0])
if len(odds) > 1:
    print("I'm Sorry Hansoo")
else:
    prefix = ''
    for i in range(0, len(words), 2):
        prefix += words[i]
    print(prefix + center + prefix[::-1])