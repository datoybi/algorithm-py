'''
맞았습니다!
뒤에서부터 count 하는 아주 좋은 방법이 있다는 걸 몰랐당..
아직 갈길이 멀다.
주식 하나를 산다.
원하는 만큼 가지고 있는 주식을 판다.
아무것도 안한다.
'''

import sys

for _ in range(int(sys.stdin.readline())):
    N = int(sys.stdin.readline())
    chart = list(map(int, sys.stdin.readline().split()))
    max_value = chart[-1]
    profit = 0

    for i in range(N-1, -1, -1):
        if chart[i] > max_value:
            max_value = chart[i]
        else:
            profit += max_value - chart[i]
    print(profit)

# 시간초과..
# import sys

# for _ in range(int(sys.stdin.readline())):
#     N = int(sys.stdin.readline())
#     chart = list(map(int, sys.stdin.readline().split()))
#     max_value = max(chart)
#     profit = 0
#     # print(max_value)

#     for i in range(N):
#         # print(chart, profit, max_value)
#         if chart[i] == max_value and i+1 < N:
#             max_value = max(chart[i+1:])
#         else:
#             profit += max_value - chart[i]
#     print(profit)
