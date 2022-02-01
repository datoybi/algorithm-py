'''
맞았습니다!
높이가 N인 피자탑을
높이가 1인 피자탑들로 분리시켜야 한다
갑이 고른 피자탑의 높이가 A이고, 
갑이 이 피자탑을 높이 B인 피자탑과 높이 C인 피자탑으로 분리했다면, 
갑은 이때 B * C만큼의 즐거움을 느낍니다

dp로 어캐풀징..
'''

import sys

n = int(sys.stdin.readline())
dp = [0] * 11
dp[1] = 0; dp[2] = 1

for i in range(3, n+1):
    m = i//2
    dp[i] = m * (i-m) + dp[m] + dp[i-m]

print(dp[n])

# import sys
# n = int(sys.stdin.readline())
# ans = 0
# for i in range(n):
#     ans += i
# print(ans)