# 맞았습니다!

import sys

for _ in range(int(sys.stdin.readline())):
    str1, str2 = map(str, sys.stdin.readline().split())
    answer = list()

    for i in range(len(str1)):
        x, y = ord(str1[i])-64, ord(str2[i])-64 #A=1..

        if x <= y:
            answer.append(str(y - x))
        else:
            answer.append(str(y+26 - x))

    print('Distances:', ' '.join(answer))