'''
맞았습니다! 
힌트를 보고 알아챘다.. 
포인트는 일단 중복제거를 하는거고 그 뒤에 갯수를 세는것이다. min(bcnt, rcnt) + 1을 해주면 된다..
어렵당 ㅠ 왜 이런 쪽으로 생각이 잘 안날꽈..
연속된 임의의 문제들을 선택한다.
선택된 문제들을 전부 원하는 같은 색으로 칠한다.
6
BRBBRR
answer: 3
6
BRRRRB
answer: 2

'''

import sys

N = int(sys.stdin.readline())
a = list(sys.stdin.readline().rstrip())
flag = a[0]
Bcnt, Rcnt = 0, 0

if a[0] =='B':
    Bcnt += 1
else:
    Rcnt += 1

for i in range(1, len(a)):
    if flag != a[i]:
        if a[i] =='B':
            Bcnt += 1
        else:
            Rcnt += 1
        flag = a[i]
        
# print(Bcnt, Rcnt)
print(min(Bcnt, Rcnt) + 1)




# import sys

# N = int(sys.stdin.readline())
# a = list(sys.stdin.readline().rstrip())
# flag = a[0]
# cnt = 0

# for i in range(len(a)):
#     if flag != a[i]:
#         cnt += 1
#         flag = a[i]
# e = 0
# s = a.index('B')
# for i in range(len(a)-1, -1, -1):
#     if a[i] == 'B':
#         e = i
#         break

# count = 0
# if e == len(a)-1:
#     count = 1
# else:
#     count = 2
# tmp = a[s:e+1]
# flag = 'B'

# for j in range(len(tmp)):
#     if tmp[j] != 'B':
#         if flag != 'R':
#             count += 1
#             flag = 'R'
#     else:
#         flag = 'B'

# # R
# e = 0
# s = a.index('R')
# for i in range(len(a)-1, -1, -1):
#     if a[i] == 'R':
#         e = i
#         break

# count2 = 0
# if e == len(a)-1:
#     count2 = 1
# else:
#     count2 = 2
# tmp = a[s:e+1]
# flag = 'R'

# for j in range(len(tmp)):
#     if tmp[j] != 'R':
#         if flag != 'B':
#             count2 += 1
#             flag = 'B'
#     else:
#         flag = 'R'
        

# print(min(count, cnt, count2))
        

