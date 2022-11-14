exclude = ['A', 'J', 'V']

n = int(input())
string = input().strip()
bitecode = ''.join(list(filter(lambda x: x not in exclude, string)))
print('nojava') if not bitecode else print(bitecode)
    
