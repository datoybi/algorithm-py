# 맞았습니다!

n = int(input())
dp = [0] * 117
dp[1] = dp[2] = dp[3] = 1

for i in range(4, n+1):
    dp[i] = dp[i-1] + dp[i-3]

print(dp[n])