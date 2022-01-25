'''
맞았습니다!
'''

import sys

lst = [0 for _ in range(21)]

def fibonacci(num):
    if num == 0: return 0
    if num == 1: return 1
    if num == 2: return 1
    if lst[num] == 0:
        lst[num] = fibonacci(num-1) + fibonacci(num-2)
    return lst[num]

print(fibonacci(int(sys.stdin.readline())))