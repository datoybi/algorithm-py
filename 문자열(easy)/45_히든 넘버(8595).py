# 맞았습니다!

import sys

N, word = int(sys.stdin.readline()), sys.stdin.readline().rstrip()
tmp, lst, num = 0, list(), ''

for i in range(len(word)):
    if word[i].isnumeric(): # 숫자면
        if tmp == i-1: # 연속된 수면
            num += word[i] # num에 추가
        else: # 연속되지 않으면
            num += word[i] # num에 추가
            tmp = i # tmp를 현재 번지로
        if i == len(word)-1 and num != '': # 내 코드는 후처리를 해주는 코드여서 마지막 게 있으면 그것도 처리도 해주었다.
            lst.append(num)
        # print(num)
    else: # 숫자가 아니면
        if num != '': # num이 있으면 lst에 추가
            lst.append(num)
            num = ''

# print(lst)
sum = 0
for i in lst:
    sum += int(i)

print(sum)