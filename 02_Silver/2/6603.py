"""
K <= 12 
2^12 = 4096 (고른다 / 고르지 않는다.)

go(a, index, cnt)
a : 입력으로 주어진 수
index : 선택할지 말지 결정해야 하는 인덱스
cnt : 현재까지 포함한 수의 개수

1) 정답을 찾은 경우 : cnt == 6
2) 불가능한 경우 : 문제 조건 위배 / 더 이상 선택할 수 없을 때 ( index == a.size)
3) 다음 경우 호출 : index 번째를 선택했다. go(a, index + 1, cnt + 1)
                    index 번째를 선택하지 않았다. go(a, index+1, cnt)
"""

import sys
input = sys.stdin.readline

lotto = []
def solve(n, index, cnt):
    if cnt == 6:
        print(*lotto, sep=' ')
        return
    
    if index == len(n):
        return
    
    lotto.append(n[index])
    solve(n, index + 1, cnt + 1)
    lotto.remove(n[index])
    solve(n, index + 1, cnt)

while True:
    array = list(map(int, input().strip().split()))
    k = array[0]
    if k == 0:
        break
    numbers = array[1:]
    lotto = []
    solve(numbers, 0, 0)
    print()