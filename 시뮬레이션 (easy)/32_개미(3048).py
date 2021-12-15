# 맞았습니다!

import sys, copy

N1, N2 = list(map(int, sys.stdin.readline().split()))
ant1, ant2 = sys.stdin.readline().rstrip(), sys.stdin.readline().rstrip()

ant1 = ant1[::-1] 
order = list(ant1 + ant2)
new_order = copy.deepcopy(order)

for i in range(int(sys.stdin.readline())):
    for j in range(len(order)-1):
        if order[j] in ant1 and order[j+1] in ant2:
            new_order[j], new_order[j+1] = new_order[j+1], new_order[j] #새로운 order에서는 교환
    # print(order, new_order)
    order = copy.deepcopy(new_order) # 기존꺼에 새로운거 복사

for i in order:
    print(i, end='')
