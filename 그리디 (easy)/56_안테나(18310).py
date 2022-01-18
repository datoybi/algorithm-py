'''
안테나는 집이 위치한 곳에만 설치할 수 있고, 논리적으로 동일한 위치에 여러 개의 집이 존재하는 것이 가능하다.
안테나를 각 지점에서 왼쪽, 오른쪽으로 움직일 때 답이 어떻게 변할 지 생각해보면 어떨 때가 최적인지 알 수 있을 거에요
'''

import sys

N = int(sys.stdin.readline())
house = list(map(int, sys.stdin.readline().split()))
result = 0
total = 100000
total_house = sum(house)

for i in range(N):
    total_tmp = abs(total_house - house[i] * (N-1) - house[i])
    print(total_tmp)
    if total > total_tmp:
        total = total_tmp
        result = house[i]

print(result)


# 시간초과
# import sys

# N = int(sys.stdin.readline())
# house = list(map(int, sys.stdin.readline().split()))
# house.sort()
# value = 0
# total = 100000
# tmp = 0
# # print(N, house)

# for i in range(N):
#     total_tmp = 0
#     for j in range(N):
#         total_tmp += abs(house[i] - house[j])
#     if total > total_tmp:
#         total = total_tmp
#         value = house[i]

# print(value)