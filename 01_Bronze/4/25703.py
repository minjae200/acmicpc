n = int(input())

default = 'int a;\nint *ptr = &a;'
print(default)

for i in range(2, n+1):
    op = '*' * i
    print(f'int {op}ptr{i} = &ptr{i-1};' if i != 2 else f'int {op}ptr{i} = &ptr;')