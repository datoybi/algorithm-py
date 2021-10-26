# 문제를 잘못 읽음 ㅠ
# 
# lst = ['TATGATAC','TAAGCTAC','AAAGATCC','TGAGATAC','TAAGATGT']
count = list()
str = ''
cnt = 0

for i in range(0, len(lst)): #0~4
    cnt = 0
    str = lst[i]
    for j in range(0, len(lst)):
        # print(lst[i])
        tmp1 = list(lst[i])
        tmp2 = list(lst[j])
        print(tmp1, tmp2)
        for z in range(0,8):
            # print(tmp1[z], tmp2[z])
            if tmp1[z] != tmp2[z]:
                cnt += 1
                print(tmp1[z], tmp2[z], z)
                print(cnt)

    count.append((str, cnt))
    print('\n')

print(count)
        
         

#     tmp_lst = str(list(i))
#     print(tmp_lst)

# #   for j in tmp_lst:
# #     print('j: ' , j)

# print(lst[0])
# print(lst[0][0])

# for i in range(0, len(lst)):
#     print(lst[0i)