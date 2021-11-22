'''
    맞았습니다!
    
    일단 문자들을 받고 추가로 느낌표를 넣어줬는데 이건 계속 런타임 에러가 났다.(index error)
    그래서 배열에 미리 '!'를 넣어두고 추가하는 방식으로 진행했다.
'''

import sys

answer = list()

for _ in range(5):
    tmp_lst = ['!' for _ in range(15)] # 느낌표 미리 넣어두기
    lst = list(map(str, sys.stdin.readline().rstrip()))
    for i in range(len(lst)):
        tmp_lst[i] = lst[i]

    answer.append(tmp_lst)

for i in range(15): # 출력시 느낌표는 출력하지 않기
    for j in range(5):
        if answer[j][i] != '!':
            print(answer[j][i], end='')
        

# # 자꾸 런타임 에러 index error 나는데 왤까ㅠ string도 list도 계속 난다.
# import sys

# lst = list()
# for i in range(5):
#     lst.append(list(map(str, sys.stdin.readline().rstrip())))

# # print(lst)

# for i in range(5): # 길이가 제멋대로면 에러나니까 공백을 특수문자로 채워주기
#     if len(lst[i]) < 14:
#         add = ''
#         for j in range(15-len(lst[i])):
#             # add += '!'
#             lst[i].append('!')


# # print(lst)       
# answer = ''
# for i in range(len(lst[0])): # 출력시 특수문자로 채운 공백은 출력하지 않기
#     for j in range(len(lst)):
#         if lst[j][i] != '!':
#             answer += lst[j][i] 
        

# print(answer, end='')

