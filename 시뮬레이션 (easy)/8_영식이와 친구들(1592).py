'''
맞았습니다!

    N 사람 수
    M 공을 받는 횟수
    L 던질 길이

'''

import sys

N, M, L = list(map(int,sys.stdin.readline().split()))
# print(N, M, L)
lst = list()
for i in range(N):
    lst.append([i+1, 0])

count, i = 0, 0

while True:
    # print(lst, lst[i][0], i)
    lst[i][1]+=1
    tmp = lst[i][1]
    if tmp == M: break
    count += 1

    if tmp % 2 == 1: # 홀수면
        i = i + L
        if i > N-1:
            i = i - N 
    elif tmp % 2 == 0: # 짝수면
        i = i - L
        if i < 0:
            i = i + N 

print(count)

