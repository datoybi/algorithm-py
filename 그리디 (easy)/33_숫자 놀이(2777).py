'''
양의 정수
'''

import sys

a, b = list(map(int, sys.stdin.readline().split()))
lst = list(map(int, sys.stdin.readline().split()))

for i in lst:
    print(i-(a*b), end=' ')