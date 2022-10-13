score = list(map(int, input().split()))
score.sort()

print(abs(score[3] + score[0] - (score[2] + score[1])))