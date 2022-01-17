'''
두 카드는 인접한 카드여야 한다
업그레이드 된 카드 A의 레벨은 변하지 않는다.

두 카드 레벨의 합만큼 골드를 받는다.
'''

import sys
int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
lst.sort(reverse=True)
gold, value = 0, 0

for i in range(1, len(lst)):
    value = max(value, lst[i-1], lst[i])
    gold += value + lst[i]

print(gold)