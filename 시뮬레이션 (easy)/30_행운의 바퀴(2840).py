'''
맞았습니다!
바퀴를 두바퀴 이상 돌리는 경우의 수를 놓쳤음!!! 결국 해냈다..


    바퀴를 K번 돌림 
    어떤 글자에서 멈추었는지 종이에 적는다 
    종이를 바탕으로 바쿠에 적은 알파벳 알아내기 

    바퀴의 칸의 수 N, 바퀴를 돌리는 횟수 k
    화살표가 가리키는 글자가 몇번 바뀌었는지 나타내는 S, 회전을 멈추었을 때 가리키던 글자

    마지막 회전에서 화살표가 가리키는 문자부터 시계방향으로 알파벳 출력 모르는 칸은 ? 행운의 바퀴가 없으면 !

'''

import sys

N, K = list(map(int, sys.stdin.readline().split()))
lst = ['?' for _ in range(N)]
flag, now = True, 0
last_word, last_idx = '', 0

for j in range(K):
    S, word = sys.stdin.readline().split()
    now = (now + int(S)) % N
    if lst[now] == '?': 
        lst[now] = word
    else:
        if lst[now] != word:
            flag = False
    if j == K-1:
        last_word = word
# print(now, word, lst, flag)
# 출력
if flag == False:
    print("!")
else:
    lst.reverse()
    for i in range(N):
        if lst[i] == last_word:
            last_idx = i
        if lst[i] != '?' and lst.count(lst[i]) != 1:
            print('!')
            exit(0)
    for i in lst[last_idx:]:
        print(i, end='')
    for i in lst[0:last_idx:]:
        print(i, end='')





# # 왜 런타임 indexof 에러?! 아놔
# import sys

# N, K = list(map(int, sys.stdin.readline().split()))
# lst = ['?' for _ in range(N+1)]
# flag, now = True, 0
# last_word, last_idx = '', 0

# for j in range(K):
#     S, word = sys.stdin.readline().split()
#     now += int(S)
#     if now > N: # 돌림판의 개수를 넘어가면 
#         now -= N
#     if lst[now] == '?': 
#         lst[now] = word
#     else:
#         if lst[now] != word:
#             flag = False
#     if j == K-1:
#         last_word = word
#     # print(now, word, lst, flag)

# print(lst, flag)
# # 출력
# if flag == False:
#     print("!")
# else:
#     del lst[0]
#     lst.reverse()
#     for i in range(N):
#         if lst[i] == last_word:
#             last_idx = i
#         if lst[i] != '?' and lst.count(lst[i]) != 1:
#             print('!')
#             exit(0)
#     for i in lst[last_idx:]:
#         print(i, end='')
#     for i in lst[0:last_idx:]:
#         print(i, end='')
