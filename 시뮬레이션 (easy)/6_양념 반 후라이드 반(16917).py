'''
맞았습니다!
    양념        A
    후라이드    B
    반반        C

양념치킨 최소 X
후라이드치킨 최소 Y
반반도 가능

치킨을 구매하는 금액의 최솟값

내가 생각한 개념
후라이드랑 양념을 따로 사는 경우와 반반을 2개 사는 경우를 분리해서 생각했음
'''

import sys

A, B, C, X, Y = list(map(int, sys.stdin.readline().split()))
lst, sum = list(), 1

if C*2 <= A+B: # 따로 사는게 더 크면 
    min_val =  min(X,Y)
    X -= min_val
    Y -= min_val
    sum = min_val*C*2
    # print(X, Y, sum, min_val)
    if X != 0:
        if C*2 < A:
            sum += C*2 * X
        else:
            sum += X*A
    elif Y != 0:
        if C*2 < B:
            sum += C*2 * Y
        else:
            sum += Y*B
        
elif C*2 > A+B: # 반반이 더 크면 
    min_val =  min(X,Y)
    X -= min_val
    Y -= min_val
    sum = min_val*A + min_val*B
    # print(X, Y, sum, min_val)

    if X != 0:
        if C*2 < A:
            sum += C*2 * X
        else:
            sum += X*A
    elif Y != 0:
        if C*2 < B:
            sum += C*2 * Y
        else:
            sum += Y*B


print(sum)  