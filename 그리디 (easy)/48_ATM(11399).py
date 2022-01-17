# 맞았습니다! 
# 이문제는 왜 실버3일까.?

import sys

int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()
total = 0

for i in range(1, len(lst)+1):
    total += sum(lst[:i])

print(total)