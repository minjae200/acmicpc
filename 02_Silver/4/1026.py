n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

array = zip(a,b)
result = 0
for da, db in array:
    result += da * db
print(result)