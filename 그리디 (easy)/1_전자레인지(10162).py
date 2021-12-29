'''
맞았습니다!

시간이 더해짐
A 5분 = 300
B 1분 = 60
C 10초 = 10

A,B,C를 누르는 횟수는 항상 최소
1 <= T <= 10000

'''

import sys

T, lst = int(sys.stdin.readline()), list()

if T >= 300: # A 처리
    lst.append(T // 300)
    T = T % 300
else:
    lst.append(0)
if T >= 60: # B 처리
    lst.append(T // 60)
    T = T % 60 
else:
    lst.append(0)
if T >= 10: # C 처리
    lst.append(T // 10)
    T = T % 10 
else: 
    lst.append(0)

if T != 0:
    print(-1)
    exit(0)
else:
    for i in lst:
        print(i, end=' ')
    


# 다른 숏코딩
# T = int(input())
# if T % 10:
#     print(-1)
# else:
#     print(T // 300, T % 300 // 60, T % 300 % 60 // 10)