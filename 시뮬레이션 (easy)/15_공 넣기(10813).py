'''
맞았습니다!
    총 바구니 N
    각각 바구니 1~N
    각각 매우 많은 공 1~N

    앞으로 M번 공을 넣으려고 한다.
    공을 넣을 때 바구니의 범위를 정하고 모두 같은 공을 넣는다
    바구니에 공이 이미 있으면 공을 빼고 새로 공을 넣는다
    공을 ㅓㄶ을 바구니는 연속되어 있어야 한다 
    M번 공을 넣은 이후에 각 바구니에 어떤 공이 들어 있는지 해라

    총 바구니 N (1 <= N <= 100) 공을 넣을 횟수 M (1 <= M <= 100)
    M개의 줄에 걸쳐서 공을 넣는 방법
    i번 바구니부터 j번 바구니까지 k번 번호가 적혀있는 공을 넣는다
'''

import sys

N, M = list(map(int, sys.stdin.readline().split()))
basket = [0] + [0 for _ in range(1, N+1)]

for _ in range(M):
    i, j, k = list(map(int, sys.stdin.readline().split()))

    for z in range(i, j+1):
        basket[z] = k
        
for i in range(1, len(basket)):
    print(basket[i], end= ' ')