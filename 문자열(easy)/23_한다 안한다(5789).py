# 맞았습니다!

import sys

for _ in range(int(sys.stdin.readline())):
    num = sys.stdin.readline().rstrip()
    
    if num[int(len(num)/2)-1] == num[int(len(num)/2)]: # 중간에서 나눈값들 구하기
        print('Do-it')
    else:
        print('Do-it-Not')
