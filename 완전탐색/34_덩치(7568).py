'''
맞았습니다!
처음에는 다른 방법으로 하다가 ... 문제가 조금 까다롭고 이해하기가 힘들게 되어 있었다. 
그래서 더 완벽히 이해를 하고, 전혀 다른 방법으로 접근하니 맞았다.

반례들 ..
2
10 20
10 21
답 1 1

4
10 20
10 20
20 30
20 20(?)

3
4 1
5 10
6 1
답 2 1 1

3
11 11
10 12
11 13
답 1 2 1

'''

n, lst = int(input()), list()

for i in range(n):  
    lst.append(list(map(int, input().split()))) # 입력

count = 0
for i in range(n): # 이중 포문을 돌려서 lst[i]보다 크면 +1하기 -> 큰사람이 있으면 등수에서 밀려남 
    tmp = 1
    for j in range(n):
        # print(lst[i], lst[j], tmp)
        if lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]:
            tmp += 1
    
    lst[i].append(tmp)
    count += tmp

for i in lst: # 출력
    print(i[2], end=' ')


   
# 처음에 시도했던.. 방법
# n, lst = int(input()), list()

# for i in range(n):  
#     lst.append(list(map(int, input().split())))  

# arranged_lst = sorted(lst, key = lambda x : [-x[0], -x[1]])
# count = 1

# print(arranged_lst)

# for i in range(1, len(arranged_lst)):
#     # print(count, i)
#     # print(arranged_lst[i-1], arranged_lst[i])
#     if arranged_lst[i-1][0] > arranged_lst[i][0] and arranged_lst[i-1][1] > arranged_lst[i][1]:
#         print('one')
#         arranged_lst[i-1].append(count)
#         count = count + 1
#     elif arranged_lst[i-1][0] >= arranged_lst[i][0] or arranged_lst[i-1][1] <= arranged_lst[i][1]:
#         print('two')
#         arranged_lst[i-1].append(count)
#     elif arranged_lst[i-1][0] <= arranged_lst[i][0] or arranged_lst[i-1][1] >= arranged_lst[i][1]:
#         print('three')
#         arranged_lst[i-1].append(count)
#     else:
#         print('four')
#         count = i
#         arranged_lst[i-1].append(count)

# print("lst : " , lst)

# # arranged_lst[-1].append(len(arranged_lst))
# if arranged_lst[-2][0] > arranged_lst[-1][0] and arranged_lst[-2][1] > arranged_lst[-1][1]:
#     arranged_lst[-1].append(count)
# else:
#     arranged_lst[-1].append(len(arranged_lst))



# print("lst : " , lst)

# for i in lst:
#     print(i[2], end=' ')


