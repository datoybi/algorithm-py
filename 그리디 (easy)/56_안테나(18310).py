'''
맞았습니다!
200000 이렇게 많은 숫자는 완전탐색으로 푸는 방법이 아니라 무슨 수학적인 방법으로 짧게
쓰면 되더라... 그걸 잘 못찾음
안테나는 집이 위치한 곳에만 설치할 수 있고, 논리적으로 동일한 위치에 여러 개의 집이 존재하는 것이 가능하다.
안테나를 각 지점에서 왼쪽, 오른쪽으로 움직일 때 답이 어떻게 변할 지 생각해보면 어떨 때가 최적인지 알 수 있을 거에요
'''


import sys

N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()

if N % 2 == 1:
    print(lst[N//2])
else:
    print(lst[(N-1)//2])




# 또 시간초과
# import sys

# N = int(sys.stdin.readline())
# lst = list(map(int, sys.stdin.readline().split()))
# result = 0
# total = 400000
# lst.sort()

# for i in range(N):
#     tmp = sum(lst[i:]) - lst[i] * (N-i) + lst[i] * i - sum(lst[:i])
#     if total > tmp:
#         total = tmp
#         result = lst[i]
# print(result)


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