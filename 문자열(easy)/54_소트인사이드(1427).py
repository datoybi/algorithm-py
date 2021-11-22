# 맞았습니다!
import sys
num = list(sys.stdin.readline().rstrip())
num.sort(reverse=True)

for i in num:
    print(i, end='')