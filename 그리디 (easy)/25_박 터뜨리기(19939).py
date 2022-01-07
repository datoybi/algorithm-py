'''
맞았습니다!
K개의 팀 
N개의 공 K개의 바구니


가장 많이 담긴 바구니와 가장 적게 담긴 바구니의 공의 개수 차이
나눠 담을 수 없는 경우에는 -1을 출력
'''

import sys

N, K = list(map(int, sys.stdin.readline().split()))
a = 0

for i in range(1, K+1):
    a += i

if N < a:
    print(-1)
    exit(0)

if (N-a) % K == 0: 
    print(K-1)
else:
    print(K)
