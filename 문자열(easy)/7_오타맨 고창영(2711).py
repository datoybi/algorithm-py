# 맞았습니다!

import sys

for _ in range(int(sys.stdin.readline())):
    index, word = sys.stdin.readline().split()
    
    print(word[:int(index)-1] + word[int(index):])
