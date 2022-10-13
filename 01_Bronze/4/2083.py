import sys
input = sys.stdin.readline

while True:
    name, age, weight = map(str, input().split())
    age = int(age)
    weight = int(weight)

    if name == '#' and age == 0 and weight == 0:
        break

    if age > 17 or weight >= 80:
        print('{} Senior'.format(name))
    else:
        print('{} Junior'.format(name))