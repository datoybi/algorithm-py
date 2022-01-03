'''
맞았습니다!
N 과일 갯수 (1 <= N <= 1000)
L 스네이크버드 초기 길이 (1 <= L <= 10000)
'''

import sys

N, L = list(map(int, sys.stdin.readline().split()))
fruits = list(map(int, sys.stdin.readline().split()))
fruits.sort()
for i in range(N):
    if L >= fruits[i]:
        L += 1
    else:
        break
print(L)