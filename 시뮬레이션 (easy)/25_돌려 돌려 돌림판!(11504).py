# 맞았습니다!

import sys

for _ in range(int(sys.stdin.readline())):
    # 입력
    N, M = list(map(int, sys.stdin.readline().split()))
    X, Y, count = '', '', 0

    tmp = list(map(str, sys.stdin.readline().split()))
    for i in range(len(tmp)):
        X += tmp[i]
    
    tmp = list(map(str, sys.stdin.readline().split()))
    for i in range(len(tmp)):
        Y += tmp[i]
    
    lst = list(map(int, sys.stdin.readline().split()))

    # 계산
    for i in range(N): # 0-7
        tmp_num = ''
        tmp = lst[i:i+M]
        if len(tmp) != M: # X,Y 자릿수만큼 빼오기
            M-len(tmp)
            for i in range(M-len(tmp)):
                tmp.append(lst[i])
        
        for i in range(len(tmp)):
           tmp_num += str(tmp[i])
        
        if int(X) <= int(tmp_num) and int(tmp_num) <= int(Y):
            count += 1

    print(count)