# 맞았습니다!

import sys

word = sys.stdin.readline().strip()
count = 0

for _ in range(int(sys.stdin.readline())):
    ring =  sys.stdin.readline().strip()

    for i in range(len(ring)):
        tmp = ring[i:len(word)+i]

        if len(tmp) < len(word):
            tmp = tmp + ring[0:len(word) - len(tmp)]

        if tmp == word:
            count += 1
            break

print(count)