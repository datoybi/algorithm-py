# 맞았습니다!
import sys

for i in range(1, int(sys.stdin.readline())+1):
    for j in range(i):
        print('*', end='')
    print()