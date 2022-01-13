'''
i번 스위치는 i의 배수 번호를 가지는 전구의 상태를 모두 반전시킨다.
'''

import sys, copy

bulb = list(sys.stdin.readline().rstrip())
print(bulb)
check = copy.deepcopy(bulb)
cnt = 0
for i in range(0,10):
    print(i)
    print('쳌' , check.count('Y'))
    if 'Y' not in check:
        cnt = i
        break
    check = copy.deepcopy(bulb)
    for j in range(len(bulb)):
        if i == 0:
            if check[j] == 'Y':
                check[j] = 'N'
            else:
                check[j] = 'Y'
        elif j % (i+1) == 0:
            if check[j] == 'Y':
                check[j] = 'N'
            else:
                check[j] = 'Y'
    print(check)

print(cnt-1)