'''
맞았습니다!
O(n)
쉬운 문제 
x번 카드와 y번 카드를 골라 그 두 장에 쓰여진 수를 더한 값을 계산한다. (x ≠ y)
계산한 값을 x번 카드와 y번 카드 두 장 모두에 덮어 쓴다.
'''

import sys

n, m = list(map(int, sys.stdin.readline().split()))
lst = list(map(int, sys.stdin.readline().split()))

for i in range(m):
    lst.sort()
    tmp = lst[0] + lst[1]
    lst[0] = tmp 
    lst[1] = tmp

print(sum(lst))