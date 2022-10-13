import sys
input = sys.stdin.readline

first = int(input())
second = int(input())

diff = second - first
if diff <= 0:
    print('Congratulations, you are within the speed limit!')
elif 1 <= diff <= 20:
    print('You are speeding and your fine is $100.')
elif 21 <= diff <= 30:
    print('You are speeding and your fine is $270.')
elif diff >= 31:
    print('You are speeding and your fine is $500.')