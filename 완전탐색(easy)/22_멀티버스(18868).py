'''
맞았습니다!
'''
M, N = map(int,input().split())
lst = list()
flag = False
count = 0

for i in range(M):
    lst.append(list(map(int, input().split())))

for i in range(M):
    for j in range(i+1, M):
        for z in range(N):
            flag = False
            if sum(lst[i][z:z+1]) - lst[i][z-1] > 0 and sum(lst[j][z:z+1]) - lst[j][z-1] > 0 :
                flag = True
            if sum(lst[i][z:z+1]) - lst[i][z-1] == 0 and sum(lst[j][z:z+1]) - lst[j][z-1] == 0 :
                flag = True
            if sum(lst[i][z:z+1]) - lst[i][z-1] < 0 and sum(lst[j][z:z+1]) - lst[j][z-1] < 0 :
                flag = True
            if flag == False:
                break

        if flag == True:
            count += 1
print(count)
