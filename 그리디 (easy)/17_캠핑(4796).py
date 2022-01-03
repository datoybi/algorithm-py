'''
맞았습니다!
연속하는 P일중 L일만 사용 할 수있다. V일짜리 휴가를 시작했다.
5 8 23
'''

import sys
n = 1
while True:
    L, P, V = list(map(int, sys.stdin.readline().split()))
    if L == 0 and P == 0 and V == 0: break
    score = V // P * L 
    if V % P <= L:
       score += V % P
    else:
        score += L
    print(f'Case {n}: {score}')
    n += 1