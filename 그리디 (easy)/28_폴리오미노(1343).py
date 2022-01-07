'''
맞았습니다!
AAAAA
BB
X만 덮기
'''


# 내 풀이는 어마어마하게 긴 코드인데 다른사람은 짧게 풀었다. 
# XXXX를 AA로 replace를 하고 XX BB rplace하는 방법으로 말이다..

p = input().replace('XXXX', 'AAAA').replace('XX','BB')
print( -1 if 'X' in p else p)


# # 내 풀이
# def calculate(idx, i):
#     if len(p[idx:i]) % 4 == 0:
#         for j in range(idx, i):
#             p[j] = 'A'
#     elif len(p[idx:i]) % 4 == 2:
#         for j in range(idx, i):
#             if j == i-2 or j == i-1:
#                 p[j] = 'B'
#             else:
#                 p[j] = 'A'
#     elif len(p[idx:i]) == 2:
#         for j in range(idx, i):
#             p[j] = 'B'
#     else:
#         print(-1)
#         exit(0)

# import sys

# p = list(sys.stdin.readline().rstrip())
# idx = 0
# for i in range(len(p)):
#     tmp = []
#     if p[i] == '.':
#         tmp = p[idx:i]
#         calculate(idx, i)
#         idx = i+1

#     if i == len(p)-1:
#         tmp = p[idx:i+1]
#         calculate(idx, i+1)
   
# for i in p:
#     print(i, end='')

