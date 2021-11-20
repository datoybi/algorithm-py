
import sys

length = int(sys.stdin.readline())
S = sys.stdin.readline().rstrip()
cnt1, cnt2 = 0, 0

for i in S:
    if i == 'e':
        cnt1 += 1
    else:
        cnt2 += 1

if cnt1 > cnt2:
    print('e')
elif cnt1 < cnt2:
    print('2')
else:
    print('yee')