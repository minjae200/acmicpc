import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().strip().split()))
operator = list(map(int, input().split()))

result = []
def solve(index, total, plus, minus, multi, divide):
    if index == N:
        result.append(total)
        return
    
    if plus > 0:
        solve(index + 1, total + A[index], plus - 1, minus, multi, divide)
    if minus > 0:
        solve(index + 1, total - A[index], plus, minus - 1, multi, divide)
    if multi > 0:
        solve(index + 1, total * A[index], plus, minus, multi - 1, divide)
    if divide > 0:
        solve(index + 1, int(total / A[index]), plus, minus, multi, divide - 1)

solve(1, A[0], operator[0], operator[1], operator[2], operator[3])
print(max(result))
print(min(result))