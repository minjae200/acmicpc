import sys
input = sys.stdin.readline

count_fib = 0
count_fibonacci = 0

def fib(n):
    global count_fib
    if (n == 1) or (n == 2):
        count_fib += 1
        return 1
    return fib(n-1) + fib(n-2)    


def fibonacci(n):
    global count_fibonacci
    cache = [ 0 ] * (n + 1)
    cache[1] = cache[2] = 1
    for i in range(3, n + 1):
        count_fibonacci += 1
        cache[i] = cache[i - 1] + cache[i - 2]
    return cache[i]

n = int(input().strip())
fib(n)
fibonacci(n)
print(count_fib, count_fibonacci)