'''
100점
'''
A, B, C, N = map(int, input().split(' '))
# A, B, C, N = 5, 9, 12, 113
flag = False

for i in range(0, 51):
    for j in range(0, 51):
        for z in range(0, 51):
            sum = i*A + j*B + z*C
            if sum == N:
                flag = True

if flag :  
    print('1')
else: 
    print('0')

