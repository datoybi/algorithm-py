# 맞았습니다!
import sys

N, lst = int(sys.stdin.readline()), list(sys.stdin.readline().rstrip())
count = 0

for i in range(len(lst)):
    if lst[i] =='S':
        count += 1
    else:
        count += 0.5

print(min(int(count)+1, N))