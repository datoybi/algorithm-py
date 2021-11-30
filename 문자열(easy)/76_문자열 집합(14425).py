# 맞았습니다!

import sys

N, M = map(int, sys.stdin.readline().split())

group = set()
for i in range(N):
    group.add(sys.stdin.readline().rstrip())

# print(group)

count = 0
for i in range(M):
    test = sys.stdin.readline().rstrip()   
    if test in group:
        count += 1

print(count)
