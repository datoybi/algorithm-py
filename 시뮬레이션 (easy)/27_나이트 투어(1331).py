'''
맞았습니다!
나이트 : 두 칸 전진 후, 전진한 방향에서 오른쪽 혹은 왼쪽

규칙
숫자나 알파벳이 +-2, 
그밖에 것이 -+1
A~F , 1~6

'''

import sys, copy

first = list(sys.stdin.readline().rstrip())
first = [ord(first[0]), int(first[1])]
count = set()
count.add(tuple(first))
flag = True
before = copy.deepcopy(first)

for i in range(35):
    now = list(sys.stdin.readline().rstrip())
    now = [ord(now[0]), int(now[1])]   
    calculate = (abs(before[0]-now[0]), abs(before[1]-now[1]))

    if calculate != (1, 2) and calculate != (2, 1): # 이전것과의 차의 절댓값이 (1,2)이거나 (2,1)이 아니라면
        flag = False    
    # print(flag)

    count.add(tuple(now))  
    before[0] = now[0]
    before[1] = now[1]

    if i == 34: # 마지막일 때 처음으로 돌아가는지 계산
        calculate = (abs(before[0]-first[0]), abs(before[1]-first[1]))
        if calculate != (1, 2) and calculate != (2, 1):
            flag = False  


if len(count) != 36 or flag == False:
    print('Invalid')
else:
    print('Valid')










# import sys, copy

# first = list(sys.stdin.readline().rstrip())
# first = [ord(first[0]), int(first[1])]
# count = set()
# count.add(tuple(first))
# flag = True
# before = copy.deepcopy(first)

# for i in range(35):
#     now = list(sys.stdin.readline().rstrip())
#     now = [ord(now[0]), int(now[1])]   
#     # print(before, now)
#     # print(before[0]-now[0], before[1]-now[1])

#     if abs(before[0]-now[0]) == 2:
#         if abs(before[1]-now[1]) != 1:
#             flag == False
#     elif abs(before[0]-now[0]) == 1:
#         if abs(before[1]-now[1]) != 2:         
#             flag == False
#     else:
#         flag == False

#     count.add(tuple(now))
#     before[0] = now[0]
#     before[1] = now[1]

#     if i == 34: # 마지막으로 돌아올 수 있는지
#         print('마지막 : ' , before, first)
#         print('마지막 :' , abs(before[0]-first[0]), abs(before[1]-first[1]))
#         if abs(before[0]-first[0]) == 2:
#             if abs(before[1]-first[1]) != 1:
#                 flag == False
#         elif abs(before[0]-first[0]) == 1:
#             if abs(before[1]-first[1]) != 2:         
#                 flag == False
#         else:
#             flag == False

#     print(flag)
#     if flag == False: 
#         print('Invalid')
#         break
#     # print(before[0]-now[0], before[1]-now[1])

# if len(count) != 36:
#     print('Invalid')

# print(sorted(count))
# print(len(count))
