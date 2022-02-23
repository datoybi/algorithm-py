# import sys

# input = sys.stdin.readline
# N = int(input())
# lst = list(map(int, input().split()))

# M = int(input())
# my = list(map(int, input().split()))

# for i in range(M):
#     print(lst.count(my[i]), end= ' ')

import sys

input = sys.stdin.readline
N = int(input())
lst = list(map(int, input().split()))
dic = dict()

for i in range(N):
    key = str(lst[i])
    if key in dic:
        dic[key] += 1 
    else:
        dic[key] = 1

M = int(input())
my = list(map(int, input().split()))

for i in range(M):
    key = str(my[i])
    if key in dic:
        print(dic[key], end= ' ')
    else:
        print(0, end= ' ')
