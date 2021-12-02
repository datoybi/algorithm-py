'''
    운동    맥박 T만큼 증가  X+T 가 M보다 작거나 같을 때만 운동가능
    휴식    맥박 R만큼 감소     1분뒤 맥박이 X-R 절대로 M보다 낮아지면 안됌

    초기맥박 m
    운동을 n분하는데 필요한 최솟값

 N  운동할 N분의 시간
 m  맥박의 최소값, 초기 맥박
 M  맥박의 최대값
 T  운동시 1분당 맥박 증가량
 R  휴식시 1분당 맥박 감소량

'''

import sys

N, m, M, T, R = list(map(int, sys.stdin.readline().split()))
time = 0
count = 0
now = m
if T > M-m or R > M-m:
    print('-1')
    
else:
    while count != N:
        # print('now : ' , now, count, time)
        if now+T <= M: # 운동
            time += 1
            count += 1
            now += T
        elif now >= m: # 휴식
            time += 1
            now -= R
            if now < m:
                now = m
            

    print(time)

        




