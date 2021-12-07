'''
맞았습니다!
    나무조각 5개 1~5까지 숫자중 하나가 쓰여져 있다.
    모든 숫자는 다섯 조각중 하나에만 쓰여있다. (각각의 나무조각에 한가지 숫자가 있다고?)
    
'''

import sys
lst = list(map(int, sys.stdin.readline().split()))

i = 0
while True:
    if i == 4:
        i = 0
    if lst[i] > lst[i+1]:
        lst[i], lst[i+1] = lst[i+1], lst[i]
        for j in lst:
            print(j, end=' ')
        print()

    if lst[0] < lst[1] < lst[2] < lst[3] < lst[4]:
        break
    else:
        i += 1