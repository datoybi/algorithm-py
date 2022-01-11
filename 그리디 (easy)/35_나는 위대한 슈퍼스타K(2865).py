'''
맞았습니다!
예선 N명
M개의 장르
점수는 실수
K명이 본선

능력의 합이 최대

예선에 참가한 사람 N , 장르 M, 본선에 뽑힐 사람 K
M개의 줄은 장르가 주어진다
N개의 (i, s) (i 참가자의 번호, s: 장르에 대한 능력) 가 주어진다

'''

import sys

N, M, K = list(map(int, sys.stdin.readline().split()))
lst = list()

for _ in range(M):
    tmp = list(map(str, sys.stdin.readline().split()))
    a, b = '', 0.0
    for i in range(len(tmp)):
        flag = False
        if i % 2 == 0:
            a = tmp[i]
        else:
            b = float(tmp[i])
            flag = True
        if flag == True:
            lst.append((a, b))

lst.sort(key = lambda x : (-x[1]))
check, cnt, score = list(), 0, 0

for i in range(len(lst)):
    if cnt == K: break
    if lst[i][0] not in check:
        cnt += 1
        score += lst[i][1]
        check.append(lst[i][0])

print(round(score,1))