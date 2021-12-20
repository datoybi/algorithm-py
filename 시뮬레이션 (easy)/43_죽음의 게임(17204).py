# 맞았습니다!
# 그래프여서 쫄았는데 의외로 쉬운 문제

import sys

N, K = list(map(int, sys.stdin.readline().split()))
lst = [0 for _ in range(N)]
order = []

for i in range(N):
    order.append(int(sys.stdin.readline()))

i, idx, count = 1, 0, -1

while True:    
    if lst[order[idx]] == 0: # 중복해서 돌면 while문 break
        lst[order[idx]] += 1
    else:
        break

    if order[idx] == K: # K와 같으면 나가기
        count = i 
        break

    idx = order[idx]
    i += 1

print(count)
