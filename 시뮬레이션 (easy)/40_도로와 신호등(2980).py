'''
어우 내가 넘 어렵게 생각하나? 좀 어렵네..
왤케 어려웠는지 모르겠다. 어떻게 구현할지 머리가 막 꼬였다. 
그래서 구현 절차 확실히 숙지하고 코드에 반영하려고 애썼다. 
핵심은 신호등이 빨간불인지를 판별하여 빨간불이면 현재 시간과 신호등의 길이만큼 뺴주면 된다. 
이거 판별은 while 무한루프를 돌려서 차례 차례 뺴준뒤 길이보다 더 짧은게 남게된 경우 빨간불이면 빨간불시간-남은 시간 
이렇게 해주었다. (파란불일경우 아무것도 안하기)
뭔가 실제로 구현하기가 어려웠다ㅠ
그래도 결국 .. 

맞았습니다!
 
신호등 개수 N, 도로의 길이 L (1 <= N <= 100, 1 <= L <= 1000)
다음 N줄에는 각 신호등의 정보가 주어진다.
D(신호등의 위치), R, G 각각 빨간색, 초록색이 지속되는 시간
신호등은 D가 증가하는 순서로 주어진다.

'''

import sys

N, L = list(map(int, sys.stdin.readline().split()))
lst = list()

for _ in range(N):
    D, R, G = list(map(int, sys.stdin.readline().split()))
    lst.append([D, R, G])

total = 0 # 총 길이
time = 0 # 걸린시간
i = 0
while True:
    if i < len(lst) and lst[i][0] == total: # 신호등이 있는 경우
        temp = time
        result = -1
        flag = True

        while True:
            if flag == True:
                if temp < lst[i][1]:
                    # print('redlight', lst[i][1] - temp)
                    result = lst[i][1] - temp # 빨간불 시간 - 찌꺼기(?) 시간 빼기
                else:
                    temp -= lst[i][1]
                    flag = False
            else: # 파란불일때
                if temp < lst[i][2]:
                    # print('greenlight', temp)
                    result = 0
                else:   
                    temp -= lst[i][2]
                    flag = True

            if result != -1:
                time += result
                break
        i += 1

    else:
        total += 1
        time += 1

    if total >= L:
        break
        
print(time)








# import sys

# N, L = list(map(int, sys.stdin.readline().split()))
# lst = list()

# for _ in range(N):
#     D, R, G = list(map(int, sys.stdin.readline().split()))
#     lst.append([D, R, G])

# total = 0 # 총 길이
# time = 0 # 시간
# i = 0
# while True:
#     print('total : ' , total, 'time : ' , time)

#     if lst[i][0] == time: # 신호등 시간이랑 현재 위치랑 같으면
#         temp = time
#         flag = True
#         check = True

        

#         while check:
#             if flag == True:
#                 if temp < lst[i][1]:
#                     print('redlight', lst[i][1] - temp)
#                     time += lst[i][1] - temp
#                     check = False
#                 else:
#                     temp -= lst[i][1]
#                     flag = False
#             else:
#                 if temp < lst[i][2]:
#                     print('greenlight', temp)
#                     check = False
#                     continue
#                 else:
#                     temp -= lst[i][2]
#                     flag = True

#         if i != len(lst)-1:
#             i += 1


#     else:
#         total += 1
#         time += 1


#     if total >= L:
#         break
        

# print(time)