'''
1년 5%
3년 20%
5년 35%

투자의 기한을 채우는 시점에 이율 반영
투자 방식은 매년 바꿀 수 있따
이율은 소수점 이하를 버림 해서 받는닼
'''
# 담에 또 풀어보기ㅠㅠ
import sys

N, year = map(int, sys.stdin.readline().split())
dp = [0] * (year+1)
dp[0] = N

for i in range(1, year+1):
    if i >= 5:
        dp[i] = max(dp[i-5] * 1.35, dp[i-3] * 1.2, dp[i-1] * 1.05)
    elif i >= 3:
        dp[i] = max(dp[i-3] * 1.2, dp[i-1] * 1.05)
    else:
        dp[i] = dp[i-1] * 1.05
    dp[i] = int(dp[i])

print(int(dp[year]))




# import sys
# N, year = list(map(int, sys.stdin.readline().split()))
# dp = [N] * year
# i = 0

# while True:
#     if year == 0: break
#     if year >= 5:
#         dp[i] = int(dp[i-1] * 1.35)
#         year -= 5
#     elif year < 5 and year >= 3:
#         dp[i] = int(dp[i-1] * 1.2)
#         year -= 3
#     else:
#         dp[i] = int(dp[i-1] * 1.05)
#         year -= 1
#     i += 1

# print(dp)
# print(max(dp))



# import sys
# N, year = list(map(int, sys.stdin.readline().split()))
# dp = [N] * year
# i = 0
# while True:
#     if year == 0: break
#     print(dp, year)
#     if year >= 5:
#         dp[i] = int(dp[i-1] * 0.35 + dp[i-1])
#         year -= 5
#     elif year < 5 and year >= 3:
#         dp[i] = int(dp[i-1] * 0.2 + dp[i-1])
#         year -= 3
#     else:
#         dp[i] = int(dp[i-1] * 0.05 + dp[i-1])
#         year -= 1
#     i += 1

# print(dp)
# print(max(dp))