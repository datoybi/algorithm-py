# 맞았습니다!
import sys

for i in range(int(sys.stdin.readline())):
    word = list(map(str, sys.stdin.readline().split()))
    print(f'Case #{i+1}:', end=' ')

    for i in range(len(word)):
        print(word[-1], end=" ")
        word.pop()
    print()
        
