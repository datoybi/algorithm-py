'''
맞았습니다!
'''

m, Seed, X1, X2 = map(int, input().split(' '))
a, c = 0, 0

for a in range(0, m): # 0~12
    for c in range(0,m):
        if (a * Seed + c) % m == X1 and (a * X1 + c) % m == X2:
            print(a , c)
            exit(0)