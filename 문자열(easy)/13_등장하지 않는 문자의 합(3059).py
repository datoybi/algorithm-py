# 맞았습니다!

import sys

for _ in range(int(sys.stdin.readline())):
    zero_lst = [0 for _ in range(100)] 
    word = sys.stdin.readline().strip()

    for i in word:
        num = ord(i)
        zero_lst[num] += 1
    
    sum = 0
    for i in range(65,91):
        if zero_lst[i] == 0:
            sum += i

    print(sum)