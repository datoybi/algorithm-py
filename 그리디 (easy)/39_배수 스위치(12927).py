'''
i번 스위치는 i의 배수 번호를 가지는 전구의 상태를 모두 반전시킨다. 
인데 왜 ?!?!?!? bulb가 y일때만 반전시켜?

문제가 이해가 되지 않는 문제이당.

'''

import sys

bulb = list(sys.stdin.readline().rstrip())
bulb.insert(0,'N')
print(bulb)
cnt = 0
for i in range(1,len(bulb)):
    print(i)
    if bulb[i] == 'Y': 
        for j in range(i, len(bulb), i):
            if j % i == 0:
                if bulb[j] == 'Y':
                    bulb[j] = 'N'
                else:
                    bulb[j] = 'Y'
        cnt += 1
    print(bulb)

print(cnt)