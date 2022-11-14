password = list('ILOVEYONSEI')
current = input().strip()
total = 0

for i in password:
    total += abs(ord(current)-ord(i))
    current = i
print(total)