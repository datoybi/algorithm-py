

import sys

variable = list(map(str, sys.stdin.readline().split()))
front, lst = variable[0], list()

for i in range(1, len(variable)):
    lst.append(variable[i][0:len(variable[i])-1]) # 예쁘게 걸러서 리스트에 다시 담기

check = ['&', '[]', '*']

for i in range(len(lst)):
    tmp = ''
    cnt = 0 # 변수 길이 측정
    for j in range(len(lst[i])-1, -1, -1): # 뒤에서부터 
        for z in range(len(check)):
            length = len(check[z])
            # print(lst[i][j:j+length])
            if check[z] == lst[i][j:j+length]: # 뒤에서 부터 check len만큼 가져와 맞는지 판별
                tmp += check[z]
                cnt = j

    if cnt != 0: # 변수길이
        print(f'{front}{tmp} {lst[i][0:cnt]};')
    else:
        print(f'{front}{tmp} {lst[i][0]};')
