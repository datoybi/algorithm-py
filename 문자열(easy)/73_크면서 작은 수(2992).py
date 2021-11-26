#  맞았습니다!

import sys, itertools
num = sys.stdin.readline().rstrip()

lst, result = list(itertools.permutations(num, len(num))), list()

for i in range(len(lst)):
    sum = ''
    for j in range(len(lst[i])):
        sum += lst[i][j]
    if int(sum) > int(num):
        result.append(int(sum))

# 출력
if result :
    print(min(result))
else:
    print(0)