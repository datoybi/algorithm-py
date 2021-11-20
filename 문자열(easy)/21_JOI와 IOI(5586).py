# 맞았습니다!

import sys

word = sys.stdin.readline().rstrip()
cnt1, cnt2 = 0, 0

for i in range(len(word)):
    if word[i:i+3] == 'JOI':
        cnt1 += 1
    if word[i:i+3] == 'IOI':
        cnt2 += 1

print(cnt1)
print(cnt2)
