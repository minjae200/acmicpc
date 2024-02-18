import sys
input = sys.stdin.readline

N = int(input().strip())
total = 0
people = []
enter = False
for _ in range(N):
    chat = input().strip()
    if chat == 'ENTER':
        enter = True
        total += len(set(people))
        people = []
        continue
    if not enter:
        continue
    people.append(chat)


total += len(set(people))

print(total)