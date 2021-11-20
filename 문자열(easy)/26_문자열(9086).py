# 맞았습니다!

import sys

for _ in range(int(sys.stdin.readline())):
    word = sys.stdin.readline().rstrip()

    print(word[0]+word[-1])