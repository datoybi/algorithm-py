'''
아 왜 이거 문제이해가 어렵지
음 A를 시작으로 D음씩 올리면서 고음을 부르는 경우는 첫항이 A, 공차가 D인 등차수열로 표현
항의 개수를 X라 할 때, 이 등차수열을 X단 고음  A = 1, D = 2인 6단 고음

음 A를 시작으로 D음씩 올라가는 X단 고음으로 가능한 가장 큰 X
'''

import sys

N, A, D = list(map(int, sys.stdin.readline().split()))
lst = list(map(int, sys.stdin.readline().split()))
print(lst)

cnt = 0
x = 0

for i in range(N):
    if lst[i] == A + (x*D):
        cnt += 1
        x += 1
    
print(cnt)
