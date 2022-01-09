'''
N개의 레벨
레벨 클리어시 점수 획득
1만큼 감소시키는 것이 1번

'''

import sys

N = int(sys.stdin.readline())
lst, check = list(), list()
for _ in range(N):
    lst.append(int(sys.stdin.readline()))

num = lst[-1]
for i in range(N):
    check.insert(0, num)
    if num > 0:
        num -= 1
cnt = 0
for i in range(N):
    cnt += lst[i] - check[i]

print(check)
print(cnt)
