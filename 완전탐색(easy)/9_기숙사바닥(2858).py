'''
맞았습니다!
'''
R, B = map(int, input().split(' '))
tot = R+B
# L, W = 0

for i in range(R, 1, -1): # 1~9
    for j in range(R, 1, -1): # 1~9
        if i*j == tot and (i+j-2)*2 == R:
            print(i, j)
            exit(0)



            



