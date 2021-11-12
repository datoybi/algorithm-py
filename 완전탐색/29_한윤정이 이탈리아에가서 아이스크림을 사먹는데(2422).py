# 아오.. 계속 시간초과 떠서 힘들어서 못하겠당........dfs로도 풀던데 다음에 내공이 더 쌓이면 해보기


# N,M = map(int,input().split())
# whole_lst, test = list(), list()

# for i in range(M): # 이거 범위틀려서 런타임에러 났었음 ㅠ
#     test.append(list(map(int, input().split())))

# count = 0

# for i in range(1, N+1):
#   for j in range(i+1, N+1):
#     for z in range(j+1, N+1):
#       whole_lst.append([i, j, z])

# # print(whole_lst)
# # print(test)
# # flag = True

# # print(whole_lst)
# for i in range(len(whole_lst)):
#   # print(i)
#   flag = True

#   for j in range(0,3):# 0 1 2 
#     for z in range(j+1,3): # 0 1 2
#       # print(whole_lst[i][j], whole_lst[i][z])

#       for k in range(M):
#         # print("test : " , test[k][0] , test[k][1])
#         if whole_lst[i][j] == test[k][0] and whole_lst[i][z] == test[k][1]:
#           flag = False
#           break

#   # print('\n')

#   if flag == True:
#     count+=1
#     # print(whole_lst[i])
# print(count)

################################################3

#         tmp_lst = list()

#         tmp_lst.append(whole_lst[i][j])
#         tmp_lst.append(whole_lst[i][j-1])
#         tmp_lst.sort()

#         for k in range(M):
#             print(test[k][0], test[k][1], tmp_lst[0], tmp_lst[1])
                
#             if tmp_lst[0] == test[k][0] and tmp_lst[1] == test[k][1]:
#                 flag = False
    
#     if flag == True:
#         count+=1
#         print(whole_lst[i])
        
# print(count)

################################################ 이렇게 줄여봐도 시간초과 난다
 
# N,M = map(int,input().split())
# whole_lst, test = list(), list()

# for i in range(M): # 이거 범위틀려서 런타임에러 났었음 ㅠ
#     test.append(list(map(int, input().split())))

# test.sort()
# count = 0

# for i in range(1, N+1):
#   for j in range(i+1, N+1):
#     for z in range(j+1, N+1):
#       for k in range(M):
#         if test[k][0] not in [i,j,z] and test[k][1] not in [i,j,z]:
#           count += 1
#           # print(i , j , z)
# print(count)

          
  
################################################

# N,M = map(int,input().split())
# whole_lst, test = list(), list()

# for i in range(M): 
#     test.append(list(map(int, input().split())))

# test.sort()
# # print(test)
# count = 0

# for i in range(1, N+1):
#   for j in range(i+1, N+1):
#     for z in range(j+1, N+1):
#       whole_lst.append([i, j, z])

# # print(whole_lst)

# for i in range (len(whole_lst)):
#   flag = True
#   # print(i)
#   # print(whole_lst[i])
#   for k in range(M): # 0 1 2
#     # print(test[k][0] , test[k][1], whole_lst[i])
#     if test[k][0] in whole_lst[i] and test[k][1] in whole_lst[i]:
#       # print("yes")
#       flag = False
#       break;

#   if flag == True:
#     count += 1
#     print(test[k][0] , test[k][1], whole_lst[i])

# print(count)


################################################ 배껴온 코드 - 봐도 왜 모르겠냐.......후
N, M = map(int, input().split())
cnt = 0
if N < 3:
    print(cnt)
else:
    unmixed = {i: [] for i in range(1, N+1)}
    for _ in range(M):
        i, j = map(int, input().split())
        unmixed[i].append(j)
        unmixed[j].append(i)

    for i in range(1, N+1):
        for j in range(i+1, N+1):
            if j in unmixed[i]:
                continue
            for k in range(j+1, N+1):
                if k in unmixed[i] or k in unmixed[j]:
                    continue
                cnt += 1
    print(cnt)
    


# 또다른코드도 모르겠음^^

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
worsts = set()

for _ in range(M):
    a, b = map(int, input().split())
    worst = 1<<(a-1)
    worst |= 1<<(b-1)
    for i in range(N):
        worsts.add(bin(worst|(1<<i)))

print(worst)

cnt = 0        
for worst in worsts:
    if worst.count('1') == 3:
        cnt = cnt + 1

print(N*(N-1)*(N-2)//6 - cnt)