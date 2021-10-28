# 문제를 잘못 읽음 ㅠ
# 
lst = ['TATGATAC','TAAGCTAC','AAAGATCC','TGAGATAC','TAAGATGT']
count = list()
str = ''
cnt = 0
distance = 0
temp = list()
temp2 = list()


for i in range(0, 8): # 0-4
    tmp = list()
    tmp_str = ''
    for j in range(0, len(lst)):
        tmp += list(lst[j][i])
        tmp_str += lst[j][i]
        # print(tmp)
    temp.append(tmp)
    temp2.append(tmp_str)

print(temp)
# print(temp2)

# print(temp[0].count('T'))

max_value = ''
max_count = 0
result_lst = list()

for i in range(len(temp)):
    print(i)
    max_value = ''
    max_count = 0
    for j in range(len(temp[0])):
        # print(temp[i][j])
        tmp_cnt = temp[i].count(temp[i][j])
        
        # tmp_value = ''
        # print(temp[i].count(j[0]))
        print(temp[i] ,temp[i][j])
        
        # print("tmp_cnt : " , tmp_cnt , " , i[j] : " , i[j])

        if max_count < tmp_cnt: 
            # print(tmp_cnt , j)
            max_count = tmp_cnt
            max_value = temp[i][j]

        elif max_count == tmp_cnt:
            if max_value > temp[i][j]:
                print(max_value , temp[i][j])
                max_value = temp[i][j]

        print("max_count : " , max_count , " , max_value : " , max_value)

    result_lst.append(max_value)
        # tmp_cnt = temp[i].count(j)   
        # print(tmp_cnt)


print(result_lst)
# for i in range(0, len(lst)): #0~4
#     cnt = 0
#     str = lst[i]
#     for j in range(0, len(lst)):
#         # print(lst[i])
#         tmp1 = list(lst[i])
#         tmp2 = list(lst[j])
#         # print(tmp1, tmp2)
#         for z in range(0,8):
#             # print(tmp1[z], tmp2[z])
#             if tmp1[z] != tmp2[z]:
#                 cnt += 1
#                 print(tmp1[z], tmp2[z], z)
#                 print(cnt)

#     count.append((str, cnt))
#     print('\n')

# print(count)
        
         

#     tmp_lst = str(list(i))
#     print(tmp_lst)

# #   for j in tmp_lst:
# #     print('j: ' , j)

# print(lst[0])
# print(lst[0][0])

# for i in range(0, len(lst)):
#     print(lst[0i)