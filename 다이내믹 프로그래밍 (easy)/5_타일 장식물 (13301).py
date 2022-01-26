# 맞았습니다!

import sys

N = int(sys.stdin.readline())
dp = [0] * (N+2)
dp[1] = 1; dp[2] = 1

for i in range(3, N+2):
    dp[i] = dp[i-1] + dp[i-2]

print(dp)
print(dp[N+1]*2 + dp[N]*2)