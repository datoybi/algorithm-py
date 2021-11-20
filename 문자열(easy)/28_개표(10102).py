# 맞았습니다!

import sys

V, a, b = int(sys.stdin.readline()), 0, 0
vote = sys.stdin.readline().rstrip()

for i in range(V):
    if vote[i] == 'A':
        a += 1
    else:
        b += 1

if a > b :
    print('A')
elif a < b :
    print('B')
elif a == b :
    print('Tie')