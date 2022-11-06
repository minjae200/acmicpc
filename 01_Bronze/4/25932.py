
for _ in range(int(input())):
    people = list(map(int, input().split()))
    zack = False
    mack = False
    if 17 in people:
        zack = True
    if 18 in people:
        mack = True
    
    print(*people)
    if zack and mack:
        print('both')
        print()
    elif zack:
        print('zack')
        print()
    elif mack:
        print('mack')
        print()
    else:
        print('none')
        print()