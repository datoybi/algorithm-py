'''
맞았습니다!
문제이해를 조금 잘못했고 어렵게 생각했다.;;

가장 왼쪽에 있는 카드부터 차례대로 한 장씩 가져올 수 있다.
그다음부터는 가져온 카드를 자신의 앞에 놓인 카드들의 가장 왼쪽, 가장 오른쪽에 놓는다.
사전 순으로 가장 빠른 문자열
'''

import sys
N = int(sys.stdin.readline())

for _ in range(N):
    int(sys.stdin.readline())
    lst = list(map(str, sys.stdin.readline().split()))
    result = [lst[0]]

    for i in range(1, len(lst)):
        if result[0] >= lst[i]: 
            result.insert(0, lst[i])
        else:
            result.append(lst[i])

    print(''.join(result))

# import sys
# N = int(sys.stdin.readline())

# for _ in range(N):
#     int(sys.stdin.readline())
#     lst = list(map(str, sys.stdin.readline().split()))
#     result = list()
#     result.append(lst[0])

#     if len(lst) == 1:
#         print(''.join(lst))
#     elif len(lst) == 2:
#         if ord(lst[0]) > ord(lst[1]):
#             print(lst[1]+lst[0])
#         else:
#             print(lst[0]+lst[1])
#     else:    
#         for i in range(1, len(lst), 2):
#             if i == len(lst)-1 and len(lst)-1 % 2 != 0:
#                 if ord(result[0]) < ord(lst[i]):
#                     result.append(lst[i])
#                 else:
#                     result.insert(0, lst[i])
#                 break
#             if ord(lst[i]) > ord(lst[i+1]):
#                 result.insert(0, lst[i+1])
#                 result.append(lst[i])
#             else:
#                 result.insert(0, lst[i])
#                 result.append(lst[i+1])

#         print(min(''.join(result), ''.join(lst)))



