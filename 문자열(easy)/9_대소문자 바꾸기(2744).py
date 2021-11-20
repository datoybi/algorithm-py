# 맞았습니다!

import sys

word = sys.stdin.readline().strip()
answer = ''

for i in word:
    if i.isupper():
       answer += i.lower()
    else:
       answer += i.upper()

print(answer)