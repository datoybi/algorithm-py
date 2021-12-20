'''
    방의 개수 : N (2~100)
    행동 횟수 M (0~100)
    동일한 행동을 여러번 할 수 있음 
    x,y : x번방부터 y번방 사이의 벽을 무너뜨림

'''


import sys

lst = [[i] for i in range(0, int(sys.stdin.readline())+1)]

for _ in range(int(sys.stdin.readline())):
    x, y = list(map(int, sys.stdin.readline().split()))
    tmp = list()

    for i in range(len(lst)): # x가 포함된 인덱스 찾기
        if x in lst[i]:
            x_idx = i

    print(lst[x_idx])
    for i in range(x,y+1):
        # print(i)
        tmp.append(i)
        # del lst[i]
    print(tmp)
    
    


    print(lst)






# import sys

# lst = [[i] for i in range(0, int(sys.stdin.readline())+1)]

# for _ in range(int(sys.stdin.readline())):
#     x, y = list(map(int, sys.stdin.readline().split()))
#     x_idx = 0
#     y_idx = 0
    
#     for i in range(len(lst)): # x가 포함된 인덱스 찾기
#         if x in lst[i]:
#             x_idx = i
#         if y in lst[i]:
#             y_idx = i

#     print('x_idx : ' , x_idx, len(lst[x_idx]))
#     print('y_idx : ' , y_idx, len(lst[y_idx]))
    
#     if len(lst[y_idx]) == 1:
#         for j in range(x+1, y+1):
#             idx = 0
#             for i in range(len(lst)): # 합치기
#                 if j in lst[i]: 
#                     idx = i
#                     lst[x_idx].append(j)
#                     for z in range(len(lst[i])): # 지우기
#                         if lst[i][z] == j:
#                             print('i : ' , i, ' , ' ,  'j : ' , j , ' , ' , 'lst[i][z] : ' , lst[i][z])
#                             if len(lst[i]) == 1:
#                                 print('del lst[i] : ' , lst[i])
#                                 del lst[i]
#                                 break
#                             else:
#                                 print('del lst[i][z] : ' , lst[i][z])
#                                 del lst[i][z]
#                                 break
#                         # if lst[i][z] == j:
#                         #     print('i : ' , i, ' , ' ,  'j : ' , j , ' , ' , 'lst[i][z] : ' , lst[i][z])
#                         #     if len(lst[i]) == 1:
#                         #         del lst[i]
#                         #         break
#                         #     else:
#                         #         del lst[i][z]
#                         #         break
#                     print(lst)
#                     break
#     else:


#     print(lst)
# # print(len(lst))
# print(len(lst)-1)

'''
100
6
1 9
1 8
3 10
59 60
4 70
65 95

31

10
2
6 8
1 8

8 
6
5 8
6 7
4 7
5 6
1 3
1 5

1
'''

