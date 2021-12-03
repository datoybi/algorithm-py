'''
    총 N개의 바구니 1~N까지 번호
    M번 바구니의 순서를 역순으로 만드려고 한다. 범위안의 바구니만 역순으로 바꾸려 한다 
'''

import sys

N,M = list(map(int, sys.stdin.readline().split()))
basket = [0] + [i for i in range(1, N+1)]

for _ in range(M):
    i, j = list(map(int, sys.stdin.readline().split()))
    tmp = basket[i:j+1]
    # print(tmp)
    for z in range(len(tmp)): #삭제
        del basket[i]    
    
    for z in range(len(tmp)):
        basket.insert(i, tmp[z])


for i in range(1, len(basket)):
    print(basket[i], end=' ')