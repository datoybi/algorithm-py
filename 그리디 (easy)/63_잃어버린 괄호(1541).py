'''
-만나기 전까지만 + 효력있음 
반례모음
https://www.acmicpc.net/board/view/76909

'''

import sys

lst = list(sys.stdin.readline().rstrip())
flag, idx, result = 'first', 0, 0 

for i in range(len(lst)):
    tmp = 0
    if lst[i].isdigit() == False: # -,  나오기전까지 숫자 가져오기
        tmp = int(''.join(lst[idx:i]))
        idx = i+1
    if i == len(lst)-1:
        tmp = int(''.join(lst[idx:i+1]))
    
    if lst[i].isdigit() == False or i == len(lst)-1: 
        if flag == True: # -가 나왔으면
            result -= tmp
        elif flag == False and lst[i] == '+':
            result -= tmp
        elif flag == 'first':
            result += tmp

        if lst[i] == '-':
            flag = True

print(result)


# 남의 답 - 왜 이렇게 다 더해도되는거지.?! 모르겠당..
# a = input().split('-')
# b = [sum(map(int, i.split('+'))) for i in a]
# print(a)
# print(b)
# print(b[0] * 2 - sum(b))