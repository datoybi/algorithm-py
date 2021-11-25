# 맞았습니다!

import sys

lst = list()

for _ in range(int(sys.stdin.readline())):
    num = int(sys.stdin.readline())

    if num == 0:
        del lst[-1]
    else:
        lst.append(num)

print(sum(lst))