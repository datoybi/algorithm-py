'''
맞았습니다!
정수 M에 대한 최대공약수 찾기
테스트 케이스 1<N<100
양의 정수 1<M<100 
'''

N, M = int(input()), list()
for i in range(N):
    M.append(list(map(int, input().split())))

# print(N, M) # 3 [[10, 20, 30, 40], [7, 5, 12], [125, 15, 25]]

for i in range(N): # 3
    maxval = 1
    for j in range(len(M[i])): # 두 수 중 첫번째 수 
        for z in range(j+1, len(M[i])): # 두 수 중 두번째 수 
            # print(M[i][j] , M[i][z])
            tmp = 1
            if M[i][j] < M[i][z]:
                tmp = M[i][j]
            else:
                tmp = M[i][z]
                
            while(True):
                if M[i][j] % tmp == 0 and M[i][z] % tmp == 0:
                    if maxval < tmp:
                        maxval = tmp
                        break
                tmp -= 1
                if tmp == 0: 
                    # 원래 if tmp == 1로 했었는데 그렇게 하니까 ZeroDivisionError가 났다.
                    # 아무래도 tmp이 0이 될수도 있어서 0 으로 나누게 되어서 그렇게 된 것 같다. 
                    break;

    print(maxval)

