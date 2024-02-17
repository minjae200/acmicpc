import sys
input = sys.stdin.readline

grade_table = {
    'A+': 4.5, 'A0': 4.0,
    'B+': 3.5, 'B0': 3.0,
    'C+': 2.5, 'C0': 2.0,
    'D+': 1.5, 'D0': 1.0, 'F': 0.0
}

total_score = 0
total_grade = 0
for _ in range(20):
    subject, score, grade = map(str, input().strip().split())
    if grade == 'P':
        continue
    score = float(score)
    total_score += score
    total_grade += score * grade_table[grade]

print(total_grade / total_score)