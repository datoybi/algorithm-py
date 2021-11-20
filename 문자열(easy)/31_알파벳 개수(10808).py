# 맞았습니다!

import sys

zero_lst = [0 for _ in range(123)]
word = sys.stdin.readline().rstrip()

for i in range(len(word)):
    zero_lst[ord(word[i])] += 1

for i in range(97, 123):
    print(zero_lst[i], end=' ')