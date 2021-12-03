# 맞았습니다!

import sys

num, count = int(sys.stdin.readline()), 0

while True:
    str_num = str(num)
    # print(str_num, count)

    if len(str_num) == 1:
        print(count)
        break

    sum = 1
    for i in range(len(str_num)):
        sum *= int(str_num[i])
    count += 1
    num = sum