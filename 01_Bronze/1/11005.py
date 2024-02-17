import sys
input = sys.stdin.readline

N, B = map(int, input().split())

memory = []
while N >= B:
    memory.append(N % B)
    N = N // B
if N != 0:
    memory.append(N)

memory.reverse()
for index, c in enumerate(memory):
    if c >= 10:
        c = chr(55 + c)
    memory[index] = str(c)
print(''.join(memory))