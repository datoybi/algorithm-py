'''
(x,y) (키, 몸무게)

5
55 185
58 183
88 186
60 175
46 155

2 2 1 2 5

'''

# n = int(input())
n = 5
for i in n :
    lst
lst = [
        [55, 185],
        [58, 183],
        [88, 186],
        [60, 175],
        [46, 155]
    ]

# lst.sort()

# # [[46, 155], [55, 185], [58, 183], [60, 175], [88, 186]]

arranged_lst = sorted(lst, key = lambda x : [-x[0], -x[1]])
# [[88, 186], [60, 175], [58, 183], [55, 185], [46, 155]]
# print(arranged_lst)

count = 1

for i in range(1, len(arranged_lst)):
    # print(count, i)
    # print(arranged_lst[i-1], arranged_lst[i])
    if arranged_lst[i-1][0] > arranged_lst[i][0] and arranged_lst[i-1][1] > arranged_lst[i][1]:
        arranged_lst[i-1].append(count)
        count = count + 1
    elif arranged_lst[i-1][0] >= arranged_lst[i][0] or arranged_lst[i-1][1] <= arranged_lst[i][1]:
        arranged_lst[i-1].append(count)
    elif arranged_lst[i-1][0] <= arranged_lst[i][0] or arranged_lst[i-1][1] >= arranged_lst[i][1]:
        arranged_lst[i-1].append(count)
    else:
        count = i
        arranged_lst[i-1].append(count)

arranged_lst[-1].append(len(arranged_lst))
# print(arranged_lst)

for j in range(len(arranged_lst)):
    for z in range(len(lst)):
        if arranged_lst[j] == lst[z]:
            
            print(arranged_lst[j][2], end=' ')


# for i in range(len(lst)):
#     for j in range(0, len(lst)):
#         print(i, j)