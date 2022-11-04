"""
블록 껍질 / 컨벡스 헐 (Convex hull)  - 그라함 스캔 (Graham's Scan)
"""
import sys
input = sys.stdin.readline
points = []
for _ in range(int(input())):
    x, y = map(int, input().split())
    points.append((x, y))

"""
1. 우선 기준점을 잡는다. (보통 기준점은 y좌표가 가장 작은 것을 기준으로 한다.)
2. 그리고 이 기준점으로 하여 다른 점들을 반시계 방향으로 정렬한다.(각에 따라 정렬하면 된다.)
3. 컨벡스 헐 알고리즘(그라함 스캔(Graham's Scan) 알고리즘)을 이용한다.
"""
def inclination(p1, p2):
    return p2[0] - p1[0], p2[1] - p1[1]

def ccw(p1, p2, p3):
    v, u = inclination(p1, p2) , inclination(p2, p3)
    if v[0] * u[1] > v[1] * u[0]:
        return True
    return False

def convex_hull(points):
    convex = []
    for p3 in points:
        while len(convex) >= 2:
            p1, p2 = convex[-2], convex[-1]
            if ccw(p1, p2, p3):
                break
            convex.pop()
        convex.append(p3)
    return len(convex)

answer = -2
points = sorted(points, key=lambda x: (x[0], x[1]))
answer += convex_hull(points)
points.reverse()
answer += convex_hull(points)
print(answer)