
# 남 코드
c = [[0] * 15 for i in range(5)]

for i in range(5):
    lst = list(input())
    lst_len = len(lst)
    print(lst, lst_len)
    
    for j in range(lst_len):
        c[i][j] = lst[j]
for i in range(15):
    for j in range(5):
        if c[j][i] == 0:
            continue;
        else:
            print(c[j][i], end='')











# # 자꾸 런타임 에러 index error 나는데 왤까ㅠ
# import sys

# lst = list()
# for i in range(5):
#     lst.append(sys.stdin.readline().rstrip())

# for i in range(5): # 길이가 제멋대로면 에러나니까 공백을 특수문자로 채워주기
#     if len(lst[i]) < 14:
#         add = ''
#         for j in range(15-len(lst[i])):
#             add += '!'
#         lst[i] = lst[i] + add

# # print(lst)
# answer = ''
# for i in range(len(lst[0])): # 출력시 특수문자로 채운 공백은 출력하지 않기
#     for j in range(len(lst)):
#         if lst[j][i] != '!':
#             answer += lst[j][i] 
        

# print(answer, end='')

