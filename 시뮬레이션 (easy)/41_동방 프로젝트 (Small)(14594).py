'''
    방의 개수 : N (2~100)
    행동 횟수 M (0~100)
    동일한 행동을 여러번 할 수 있음 
    x,y : x번방부터 y번방 사이의 벽을 무너뜨림

'''
import sys

# lst = [i for i in range(1, int(sys.stdin.readline())+1)]
lst = set()

for i in range(int(sys.stdin.readline())+1):
    lst.add(i)   
print(lst)

# for _ in range(int(sys.stdin.readline())):
#     x, y = list(map(int, sys.stdin.readline().split()))
#     x_idx = 0

#     for i in range(len(lst)): # 1
#         if lst[i][0] == x:
#             x_idx = i
#             break
    
#     for i in range(len(lst)):


#     # for i in range(): # 0
#     #     lst[i].append(lst[y-1][0])
#     #     del lst[y-1]
#     #     print(lst)









# # lst = [i for i in range(1, int(sys.stdin.readline())+1)]
# lst = list()

# for i in range(int(sys.stdin.readline())+1):
#     lst.append([i])   
# print(lst)

# for _ in range(int(sys.stdin.readline())):
#     x, y = list(map(int, sys.stdin.readline().split()))
#     x_idx = 0

#     for i in range(len(lst)): # 1
#         if lst[i][0] == x:
#             x_idx = i
#             break
    
#     for i in range(len(lst)):


#     # for i in range(): # 0
#     #     lst[i].append(lst[y-1][0])
#     #     del lst[y-1]
#     #     print(lst)