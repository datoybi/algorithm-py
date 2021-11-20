# 맞았습니다!
import sys

word = sys.stdin.readline().rstrip()
lst = [-1 for _ in range(123)]

for i in range(len(word)):
    if lst[ord(word[i])] == -1:
        lst[ord(word[i])] = i

for i in range(97, 123):
    print(lst[i], end=' ')