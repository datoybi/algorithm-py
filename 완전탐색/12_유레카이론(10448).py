'''
맞았습니다!
'''

test_case = int(input())
K,T = list(), 0

for i in range(0, test_case):
    K.append(int(input()))

for k in K:
    flag = False
    for i in range(1, 101):
        for j in range(1, 101):
            for z in range(1, 101):
                if i*(i+1)//2 + j*(j+1)//2 + z*(z+1)//2 == k:
                    flag = True
          
    if flag == True:
        print('1')
    elif flag == False:
        print('0')

