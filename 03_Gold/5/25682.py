import sys
input = sys.stdin.readline

N, M, K = map(int, input().strip().split())

board = [ list(input().strip()) for _ in range(N) ]

black_prefix_sum = [[ 0 for _ in range(M + 1) ] for _ in range(N + 1) ]
white_prefix_sum = [[ 0 for _ in range(M + 1) ] for _ in range(N + 1) ]

# black_prefix_sum -> 첫 보드판 문자가 'B'인경우
# B W B W << 이런식

for i in range(N):
    for j in range(M):
        if ((i + j) % 2) == 0:
            black_add = 0 if board[i][j] == 'B' else 1
        else:
            black_add = 1 if board[i][j] == 'B' else 0
        white_add = 0 if black_add else 1
        black_prefix_sum[i][j] = black_add + black_prefix_sum[i-1][j] + black_prefix_sum[i][j-1] - black_prefix_sum[i-1][j-1]
        white_prefix_sum[i][j] = white_add + white_prefix_sum[i-1][j] + white_prefix_sum[i][j-1] - white_prefix_sum[i-1][j-1]
        
ans = sys.maxsize
for i in range(N - K + 1):
    for j in range(M - K + 1):
        B_sub_sum = black_prefix_sum[i+K-1][j+K-1] - black_prefix_sum[i-1][j+K-1] - black_prefix_sum[i+K-1][j-1] + black_prefix_sum[i-1][j-1]
        W_sub_sum = white_prefix_sum[i+K-1][j+K-1] - white_prefix_sum[i-1][j+K-1] - white_prefix_sum[i+K-1][j-1] + white_prefix_sum[i-1][j-1]
        ans = min(ans, B_sub_sum, W_sub_sum)

print(ans)