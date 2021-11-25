# 맞았습니다!

import sys

sentence, word = sys.stdin.readline().rstrip(), sys.stdin.readline().rstrip()
count, i = 0, 0

while True:
    if len(word)+i > len(sentence): 
        print(count)
        exit(0)
    else:
        if word == sentence[i:len(word)+i]:
            # print('맞')
            count += 1
            i = len(word)+i
        else:
            i += 1
        