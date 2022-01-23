'''
연속된 임의의 문제들을 선택한다.
선택된 문제들을 전부 원하는 같은 색으로 칠한다.
6
BRBBRR
answer: 3
6
BRRRRB
answer: 2

'''
import sys

N = int(sys.stdin.readline())
a = list(sys.stdin.readline().rstrip())
flag = a[0]
cnt = 0

for i in range(len(a)):
    if flag != a[i]:
        cnt += 1
        flag = a[i]
e = 0
s = a.index('B')
for i in range(len(a)-1, -1, -1):
    if a[i] == 'B':
        e = i
        break

count = 0
if e == len(a)-1:
    count = 1
else:
    count = 2
tmp = a[s:e+1]
flag = 'B'

for j in range(len(tmp)):
    if tmp[j] != 'B':
        if flag != 'R':
            count += 1
            flag = 'R'
    else:
        flag = 'B'

print(min(count, cnt))
        

