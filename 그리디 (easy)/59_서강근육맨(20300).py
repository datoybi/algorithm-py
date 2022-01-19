'''
맞았습니다!

'''

import sys

N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()
value = 0

if len(lst) % 2 == 1:
    value = lst[-1]
    del lst[-1]

while True:
    if len(lst) == 0: break
    value = max(value, lst[0]+lst[-1])
    del lst[-1]
    del lst[0]

print(value)


# 좋은방법
import sys

N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
value = 0

if len(lst) % 2 == 1:
    # value = lst[-1]
    # del lst[-1] 
    lst.append(0) # 지우는 것보다 0을 넣어 sort
lst.sort()

for i in range(len(lst) // 2): 
    if len(lst) == 0: break
    value = max(value, lst[i]+lst[-i-1]) # 지우는 방법은 좋지 않고 이렇게 하는게 더나음

print(value)
