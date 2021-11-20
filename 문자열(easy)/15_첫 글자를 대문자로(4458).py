# 맞았습니다!

import sys

for _ in range(int(sys.stdin.readline())):
    word = list(sys.stdin.readline().strip())
    word[0] = word[0].upper()

    print(''.join(word))
    