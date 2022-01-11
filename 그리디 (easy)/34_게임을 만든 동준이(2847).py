'''
맞았습니다!
N개의 레벨
레벨 클리어시 점수 획득
1만큼 감소시키는 것이 1번

4
6
5
4
8
'''

import sys

N = int(sys.stdin.readline())
lst, check = list(), list()
for _ in range(N):
    lst.append(int(sys.stdin.readline()))

num = lst[-1]
check.insert(0, lst[-1])

for i in range(N-2, -1, -1):
    if num > lst[i]:
        num = lst[i]
    elif num <= lst[i]:
        num -= 1
    check.insert(0, num)

# 차 구해서 count 하기
cnt = 0
for i in range(N):
    cnt += lst[i] - check[i]
print(cnt)


'''

4
6
5
4
8

6

4
10
8
4
9

13

4
5
3
7
5

6


3
5
5
5

3
'''