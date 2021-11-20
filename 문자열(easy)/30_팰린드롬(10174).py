# 맞았습니다!

import sys

for _ in range(int(sys.stdin.readline())):
    word = input().lower() # 이거 sys로 받으니까 문제 생김
    r_word = word[::-1]

    if word == r_word:
        print('Yes')
    else:
        print('No')
