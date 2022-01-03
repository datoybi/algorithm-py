'''
맞았습니다!
하나의 이진수에서 임의의 자리의 숫자를 0 또는 1로 바꾼다.
하나의 이진수에서 서로 다른 자리에 있는 두 숫자의 위치를 바꾼다.

'''

import sys

for _ in range(int(sys.stdin.readline())):
    N, M = list(map(str, sys.stdin.readline().split()))
    diff = list()
    for i in range(len(N)):
        if N[i] != M[i]:
            diff.append(N[i])   
    print(abs(diff.count('0')-diff.count('1')) + min(diff.count('0'),diff.count('1')))
    
        

