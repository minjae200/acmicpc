import sys
input = sys.stdin.readline

jaehwan = input().strip()
doctor = input().strip()

print('go') if len(jaehwan) >= len(doctor) else print('no')