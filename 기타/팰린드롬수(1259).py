# 맞았습니다!

import sys

while True:
    num = sys.stdin.readline().rstrip()
    if num == '0': exit(0)

    if num == num[::-1]:
        print('yes')
    else:
        print('no')