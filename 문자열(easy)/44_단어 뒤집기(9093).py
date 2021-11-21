# 맞았습니다!

import sys

for _ in range(int(sys.stdin.readline())):
    sentence = sys.stdin.readline().split()

    for i in range(len(sentence)):
        tmp = sentence[i]        
        print(tmp[::-1], end=' ')
    