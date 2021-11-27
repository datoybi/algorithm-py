# 맞았습니다!

import sys

while True:
    n1, n2, n3 = map(int, sys.stdin.readline().split())
    if n1 == 0 and n2 == 0 and n3 == 0: break

    max_val, flag = max(n3,n2,n1), False
    if max_val == n3 and n2**2 + n1**2 == n3**2:
        flag = True
    elif max_val == n2 and n1**2 + n3**2 == n2**2:
        flag = True
    elif max_val == n1 and n2**2 + n3**2 == n1**2:
        flag = True

    if flag == True:
        print('right')
    else:
        print('wrong')
