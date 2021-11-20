# 맞았습니다!

import sys

for _ in range(int(sys.stdin.readline())):
    word = list(map(str, sys.stdin.readline().split()))
    print(' '.join(word[2:]), word[0] , word[1])