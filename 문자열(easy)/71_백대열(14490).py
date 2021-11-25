# 맞았습니다!

import sys 

num1, num2 = map(int, sys.stdin.readline().split(':'))

i = min(num1, num2)
while True:
    if num1 % i == 0 and num2 % i == 0:
        print(f'{num1//i}:{num2//i}')
        exit(0)
    else:
        i -= 1