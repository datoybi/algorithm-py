'''
나왜 이거 이해안돼 낼 해보자
D[i][j] = D[i-1][j] + D[i][j-1]

'''
n, m = map(int, input().split())
dp = [[0 for _ in range(1001)] for _ in range(1001)]
dp[0][0] = 1

for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = dp[i-1][j-1]
        dp[i][j] += dp[i][j-1]
        dp[i][j] %= 1e9+7

        dp[i][j] += dp[i-1][j]
        dp[i][j] %= 1e9+7

print(int(dp[n][m]))