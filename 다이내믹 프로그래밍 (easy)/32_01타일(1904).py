# 맞았습니다!

N = int(input())
dp = [0 for _ in range(N+2)]
dp[1] = 1; dp[2] = 2

for i in range(3, N+1):
    dp[i] = (dp[i-1] + dp[i-2])%15746

print(dp[N])