# 맞았습니다!

import sys

word = sys.stdin.readline().rstrip()

if word[::-1] == word:
    print('1')
else:
    print('0')