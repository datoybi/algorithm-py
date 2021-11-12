''' 
    하던거 안되어서
    permutation 함수 익힘 

'''
# n, k = int(input()), int(input())
# n_lst = list()

# for _ in range(n):
#     n_lst.append(input())

# result_set = set()

# if n > 10 or n < 4 :
#     exit(0)

# for i in range(len(n_lst)):
#     for j in range(len(n_lst)):
#         if i==j :
#             continue
#         elif k == 3: 
#             for z in range(len(n_lst)):
#                 if j==z or z==i:
#                     continue
#                 elif k == 4:
#                      for a in range(len(n_lst)):
#                         if z==a or j==z or z==i:
#                             continue
#                         else:
                            
#                             result_set.add(n_lst[i] + n_lst[j] + n_lst[z] + n_lst[a])
#                 else:
#                     # print(i, j, z)
#                     # print(n_lst[i] , n_lst[j] , n_lst[z])
#                     result_set.add(n_lst[i] + n_lst[j] + n_lst[z])
#         else:
#             # print(n_lst[i] , n_lst[j])
#             result_set.add(n_lst[i] + n_lst[j])
              
       
# print(sorted(result_set))
# print(len(result_set)) 

import itertools

n, k = int(input()), int(input())
n_lst = list()

for _ in range(n):
    n_lst.append(input())

result_set = set()

if n > 10 or n < 4 :
    exit(0)

for i in itertools.permutations(n_lst, k):
    # print(i)
    result_set.add(''.join(i))

print(len(result_set))

