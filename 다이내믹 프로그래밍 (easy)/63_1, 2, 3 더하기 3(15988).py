# 맞았습니다!

dp = [0 for _ in range(1000001)]
dp[1] = 1; dp[2] = 2; dp[3] = 4

for i in range(4, 1000001):
    # dp[i] = int((dp[i-1] + dp[i-2] + dp[i-3]) % 1e+9) 이거는 안됐다 ㅠ
    dp[i] = dp[i-1] % 1000000009 + dp[i-2] % 1000000009 + dp[i-3] % 1000000009

for _ in range(int(input())):
    n = int(input())
    print(dp[n] % 1000000009)