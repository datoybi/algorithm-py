'''

핡 어렵다. .

A와 B의 길이가 다르면, 짧은 것이 먼저 온다.
만약 서로 길이가 같다면, A의 모든 자리수의 합과 B의 모든 자리수의 합을 비교해서 작은 합을 가지는 것이 먼저온다. (숫자인 것만 더한다)
만약 1,2번 둘 조건으로도 비교할 수 없으면, 사전순으로 비교한다. 숫자가 알파벳보다 사전순으로 작다.

8
ABCD
A
AB
ABC
145C
A910
Z321
ABCDE
 '''

import sys

lst = list()
# 입력
for _ in range(int(sys.stdin.readline())):
    lst.append(list(sys.stdin.readline().rstrip()))

lst.sort() # 일단 정렬

# 각 문자들의 길이를 list에 append해주고 그 다음엔 숫자가 있는 것들 숫자 세서 append 해주기
for i in range(len(lst)):
    lst[i].append(len(lst[i])) # 길이 append
    
    sum = 0
    for j in range(len(lst[i])-1):
        if lst[i][j].isdigit(): 
            sum += int(lst[i][j])
    lst[i].append(sum) # 합 append

lst.sort(key = lambda x : [x[-2],  x[-1]]) # -2가 길이이고 -1이 sum이니까 그걸로 정렬

# 출력
for i in range(len(lst)): 
    tmp = ''
    for j in range(len(lst[i])-2):
        tmp += lst[i][j]
        # print(lst[i][j], end='')
    print(tmp)


# print(min(lst[-2]))

# for i in range(len(lst)):
#     for j in range(i+1, len(lst)):
#         if lst[i][-2] > lst[j][-2]:
#             length = min(length, lst[j][-2])

#     print(length)


# func = sorted(lst, key = lambda x : [-x[0], -x[1]])



# for i in range(len(lst)):
#     lst.append()


# lst.sort(key=len) # 짧은 길이부터 정렬
# print(lst)

# length = lst[0]
# result = list()
# i = 0
# flag = False

# while True:
#     if len(lst[i]) < len(lst[i+1]):
#         result.append(lst[i])
#         i += 1
#     elif len(lst[i]) == len(lst[i+1]):
#         j = i
#         print(j)
#         tmp_lst = list()
#         length2 = len(lst[j])
         
#         while flag == False:
#             if len(lst[j]) == len(lst[j+1]):
#                 tmp_lst.append(lst[i])
#                 j += 1

#             elif len(lst[j]) < len(lst[j+1]):
#                 tmp_lst.append(lst[i])
#                 flag == True
#                 j += 1
#             # if lst[i] lst[i+1]
#             print('t_lst : ' , tmp_lst)
#             exit(0)
#     else:


#         i += 1
#     if i >= len(lst)-1: break

# print(result)


# for i in range(len(lst)):
#     for j in range (i+1, len(lst)):
#         if len(lst[i]) >= length:

#             print(lst[i], lst[j])

















# lst = list()

# for _ in range(int(sys.stdin.readline())):
#     lst.append(sys.stdin.readline().rstrip())

# lst.sort(key=len) # 짧은 길이부터 정렬
# print(lst)

# length = lst[0]
# result = list()
# i = 0
# flag = False

# while True:
#     if len(lst[i]) < len(lst[i+1]):
#         result.append(lst[i])
#         i += 1
#     elif len(lst[i]) == len(lst[i+1]):
#         j = i
#         print(j)
#         tmp_lst = list()
#         length2 = len(lst[j])
         
#         while flag == False:
#             if len(lst[j]) == len(lst[j+1]):
#                 tmp_lst.append(lst[i])
#                 j += 1

#             elif len(lst[j]) < len(lst[j+1]):
#                 tmp_lst.append(lst[i])
#                 flag == True
#                 j += 1
#             # if lst[i] lst[i+1]
#             print('t_lst : ' , tmp_lst)
#             exit(0)
#     else:


#         i += 1
#     if i >= len(lst)-1: break

# print(result)


# for i in range(len(lst)):
#     for j in range (i+1, len(lst)):
#         if len(lst[i]) >= length:

#             print(lst[i], lst[j])
