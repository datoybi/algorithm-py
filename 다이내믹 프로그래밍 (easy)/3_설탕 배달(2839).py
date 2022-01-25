# https://myjamong.tistory.com/291
# dp로 풀어보기

import sys

lst = list()
N = int(sys.stdin.readline())
cnt, flag = N, False

for i in range((N//5)+1):
    for j in range((N//3)+1):
        if i*5 + j*3 == N:
            cnt = min(cnt, i+j)
            flag = True
            
print(-1 if flag == False else cnt)