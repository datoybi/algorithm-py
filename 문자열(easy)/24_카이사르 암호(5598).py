# 맞았습니다!

import sys

word, answer = sys.stdin.readline().rstrip(), ''

for i in word:
    if i == 'A':
        answer += 'X'
    elif i == 'B':
        answer += 'Y'
    elif i == 'C':
        answer += 'Z'
    else:
        answer += chr(ord(i)-3)

print(answer)
